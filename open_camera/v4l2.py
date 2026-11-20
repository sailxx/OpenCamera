"""Internal interface to v4l-utils. All process invocations use argument arrays."""

from dataclasses import dataclass, field
from fractions import Fraction
from pathlib import Path
import os
import re
import shutil
import subprocess


RAW_FORMATS = {"YUYV": "YUY2", "UYVY": "UYVY", "NV12": "NV12",
               "YU12": "I420", "YV12": "YV12", "RGB3": "RGB", "BGR3": "BGR"}
COMPRESSED_FORMATS = {"MJPG": "image/jpeg", "JPEG": "image/jpeg", "H264": "video/x-h264"}


@dataclass(frozen=True)
class Device:
    path: str
    name: str
    test: bool = False

    @property
    def label(self):
        return self.name if self.test else f"{self.name}  ·  {self.path}"


@dataclass(frozen=True)
class Mode:
    fourcc: str
    width: int
    height: int
    fps: Fraction

    @property
    def label(self):
        rate = f"{float(self.fps):.3f}".rstrip("0").rstrip(".")
        return f"{self.width} × {self.height}  ·  {rate} FPS  ·  {self.fourcc}"

    @property
    def caps(self):
        media = COMPRESSED_FORMATS.get(self.fourcc)
        if media is None:
            media = f"video/x-raw,format={RAW_FORMATS[self.fourcc]}"
        return f"{media},width={self.width},height={self.height},framerate={self.fps.numerator}/{self.fps.denominator}"


TEST_DEVICE = Device("", "GStreamer test pattern", test=True)
TEST_MODES = tuple(Mode("RGB3", 1280, 720, Fraction(rate)) for rate in (30, 60, 120))


@dataclass
class Control:
    name: str
    kind: str
    value: int
    minimum: int = 0
    maximum: int = 1
    step: int = 1
    flags: frozenset[str] = frozenset()
    choices: dict[int, str] = field(default_factory=dict)

    @property
    def label(self):
        return self.name.replace("_", " ").capitalize()

    @property
    def writable(self):
        return not self.flags.intersection({"inactive", "disabled", "read-only", "grabbed"})


def invoke(path, *arguments):
    if not re.fullmatch(r"/dev/video[0-9]+", path):
        raise ValueError("Invalid V4L2 device path")
    try:
        result = subprocess.run(
            ["v4l2-ctl", "--device", path, *arguments],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
            timeout=3, check=False, env={**os.environ, "LC_ALL": "C"},
        )
    except FileNotFoundError as error:
        raise RuntimeError("Install v4l-utils to detect cameras and change hardware controls.") from error
    except subprocess.TimeoutExpired as error:
        raise RuntimeError(f"Camera did not respond: {path}") from error
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or f"Could not access {path}")
    return result.stdout


def scan_devices():
    if shutil.which("v4l2-ctl") is None:
        return [], ["Install v4l-utils to detect cameras and change hardware controls."]
    devices, issues = [], []
    paths = sorted(Path("/dev").glob("video[0-9]*"), key=lambda path: path.name)
    for path in paths:
        if not re.fullmatch(r"video[0-9]+", path.name):
            continue
        try:
            formats = invoke(str(path), "--list-formats-ext")
            if not re.search(r"Type:\s+Video Capture(?: Multiplanar)?\s*\n", formats):
                continue
            if not re.search(r"\[\s*\d+\]:", formats):
                continue
        except RuntimeError as error:
            issues.append(str(error))
            continue
        try:
            name = (Path("/sys/class/video4linux") / path.name / "name").read_text(
                encoding="utf-8", errors="replace"
            ).strip()
        except OSError:
            name = path.name
        devices.append(Device(str(path), name or path.name))
    return devices, issues


def parse_modes(output):
    modes = set()
    fourcc, dimensions = None, None
    for line in output.splitlines():
        pixel = re.search(r"\[\s*\d+\]:\s*'([^']+)'", line)
        size = re.search(r"Size:\s+Discrete\s+(\d+)x(\d+)", line)
        interval = re.search(r"Interval:\s+Discrete.*?\((\d+(?:\.\d+)?) fps\)", line)
        if pixel:
            fourcc, dimensions = pixel[1], None
        elif "Size:" in line:
            dimensions = (int(size[1]), int(size[2])) if size else None
        elif interval and dimensions and all(dimensions) and fourcc in (RAW_FORMATS | COMPRESSED_FORMATS):
            rate = Fraction(interval[1])
            if rate <= 0:
                continue
            ntsc = Fraction(round(rate * 1001 / 1000) * 1000, 1001)
            if rate.denominator != 1 and abs(ntsc - rate) < Fraction(1, 1000):
                rate = ntsc
            modes.add(Mode(fourcc, *dimensions, rate))
    return sorted(modes, key=lambda mode: (-mode.width * mode.height, -mode.fps, mode.fourcc))


def parse_controls(output):
    controls, current = [], None
    for line in output.splitlines():
        match = re.match(r"\s*(\w+)\s+0x[\da-fA-F]+\s+\((\w+)\)\s*:\s*(.*)", line)
        if match:
            current = None
            name, kind, details = match.groups()
            values = {key: int(value) for key, value in re.findall(r"\b(\w+)=(-?\d+)", details)}
            if kind not in {"int", "bool", "menu", "intmenu"} or "value" not in values:
                continue
            flags = details.partition("flags=")[2]
            current = Control(name, kind, values["value"], values.get("min", 0),
                              values.get("max", 1), max(1, values.get("step", 1)),
                              frozenset(flag.strip() for flag in flags.split(",") if flag.strip()))
            controls.append(current)
        elif current and current.kind in {"menu", "intmenu"}:
            option = re.match(r"\s+(-?\d+):\s+(.+)", line)
            if option:
                current.choices[int(option[1])] = option[2]
    return controls


def inspect_device(device):
    if device.test:
        return list(TEST_MODES), [], []
    issues = []
    try:
        modes = parse_modes(invoke(device.path, "--list-formats-ext"))
    except RuntimeError as error:
        modes = []
        issues.append(str(error))
    try:
        controls = parse_controls(invoke(device.path, "--list-ctrls-menus"))
    except RuntimeError as error:
        controls = []
        issues.append(str(error))
    return modes, controls, issues


def write_control(device, control, value):
    if not re.fullmatch(r"\w+", control.name) or not control.writable:
        raise ValueError("Control is not writable")
    value = int(value)
    if control.kind in {"menu", "intmenu"}:
        valid = value in control.choices
    elif control.kind == "bool":
        valid = value in (0, 1)
    else:
        valid = control.minimum <= value <= control.maximum and not (value - control.minimum) % control.step
    if not valid:
        raise ValueError(f"Unsupported value for {control.label}")
    invoke(device.path, "--set-ctrl", f"{control.name}={value}")
