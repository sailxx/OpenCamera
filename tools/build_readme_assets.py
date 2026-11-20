"""Regenerate the GitHub README panels from the checked-in design assets."""

from base64 import b64encode
from html import escape
from io import BytesIO
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "readme"
WIDTH = 880
WHITE = "#f2f6fc"
MUTED = "#aeb9ca"
BLUE = "#83bcff"


def text(x, y, value, size=15, color=WHITE, weight=400):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" '
            f'font-weight="{weight}">{escape(value)}</text>')


def rect(x, y, width, height, fill, radius=14, stroke="none"):
    return (f'<rect x="{x}" y="{y}" width="{width}" height="{height}" '
            f'rx="{radius}" fill="{fill}" stroke="{stroke}"/>')


def panel(name, height, title, contents, width=WIDTH):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}"
 viewBox="0 0 {width} {height}" role="img" aria-label="{escape(title, quote=True)}">
 <title>{escape(title)}</title>
 <style>text {{font-family: "Golos Text","Segoe UI",system-ui,sans-serif}}</style>
 <defs>
   <linearGradient id="ground" x2="0" y2="1" gradientUnits="objectBoundingBox">
     <stop stop-color="#141920"/><stop offset="1" stop-color="#080c13"/>
   </linearGradient>
   <radialGradient id="light"><stop stop-color="#276dde" stop-opacity=".29"/>
     <stop offset="1" stop-color="#276dde" stop-opacity="0"/></radialGradient>
   <linearGradient id="action"><stop stop-color="#1768ce"/><stop offset="1" stop-color="#123c76"/></linearGradient>
   <clipPath id="outer"><rect width="{width}" height="{height}" rx="21"/></clipPath>
 </defs>
 <g clip-path="url(#outer)">
   {rect(0, 0, width, height, 'url(#ground)', 21)}
   <ellipse cx="{width * .84}" cy="{height * .36}" rx="{width * .59}" ry="{height * .91}" fill="url(#light)"/>
   {contents}
 </g>
 {rect(.5, .5, width - 1, height - 1, 'none', 21, '#273346')}
</svg>
'''
    (OUT / f"{name}.svg").write_text(svg, encoding="utf-8")


def header(kicker, title):
    return text(32, 40, kicker, 12, BLUE, 700) + text(32, 81, title, 31, WHITE, 750)


def feature(x, y, width, title, first, second):
    return (rect(x, y, width, 96, "#141d2a", 13, "#27354a")
            + rect(x + 15, y + 15, 7, 7, "#539bff", 3)
            + text(x + 31, y + 25, title, 16, WHITE, 700)
            + text(x + 16, y + 53, first, 14, MUTED)
            + text(x + 16, y + 74, second, 14, MUTED))


def screenshot():
    with Image.open(ROOT / "design" / "open-camera-hud-preview.png") as source:
        frame = source.convert("RGB")
        frame.thumbnail((990, 742))
        encoded = BytesIO()
        frame.save(encoded, format="JPEG", quality=86, optimize=True)
    return b64encode(encoded.getvalue()).decode("ascii")


def hero():
    inner = header("LINUX CAMERA WORKBENCH", "Your camera,")
    inner += text(32, 131, "in your control.", 41, BLUE, 760)
    inner += text(33, 172, "Preview a V4L2 camera, choose its", 16, MUTED)
    inner += text(33, 197, "capture mode and adjust driver controls.", 16, MUTED)
    inner += feature(32, 231, 297, "From source", "Native GTK 4 and libadwaita", "with a local GStreamer pipeline.")
    inner += rect(351, 34, 498, 362, "#0a101a", 17, "#3d5575")
    inner += text(369, 59, "INTERACTIVE DESIGN PROTOTYPE", 11, BLUE, 700)
    inner += '<clipPath id="shot"><rect x="365" y="70" width="470" height="312" rx="9"/></clipPath>'
    inner += (f'<image x="365" y="70" width="470" height="312" '
              f'preserveAspectRatio="xMidYMin slice" clip-path="url(#shot)" href="data:image/jpeg;base64,{screenshot()}"/>')
    panel("hero", 423, "Open Camera. A native Linux camera workbench and its interface prototype.", inner)


def cards(name, kicker, title, items):
    content = header(kicker, title)
    for index, item in enumerate(items):
        content += feature(32 + (index % 2) * 414, 107 + (index // 2) * 110, 402, *item)
    panel(name, 125 + ((len(items) + 1) // 2) * 110, title, content)


def button(name, label, primary=False):
    contents = rect(1, 1, 176, 46, "url(#action)" if primary else "#131b28", 12, "#344d70")
    contents += '<path d="M19 24h12m-5-5 5 5-5 5" fill="none" stroke="#a7ceff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>'
    contents += text(42, 29, label, 14, WHITE, 700)
    panel(name, 48, label, contents, width=178)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    hero()
    button("btn-linux", "Run on Linux", primary=True)
    button("btn-design", "View the design")
    button("btn-roadmap", "See the roadmap")
    cards("features", "FEATURES", "Inside the workbench", (
        ("Camera discovery", "Select a V4L2 device and rescan", "after connecting a USB webcam."),
        ("Live preview", "Start and stop a local GStreamer stream.", "See the rate measured at capture."),
        ("Capture modes", "Use automatic negotiation or select", "an advertised format, size and rate."),
        ("Hardware controls", "Adjust driver-reported values, switches", "and menus, then read the values back."),
        ("Diagnostics", "Find missing dependencies and", "inspect camera access or stream errors."),
        ("Appearance", "Follow the desktop style or select", "light or dark appearance."),
    ))
    cards("workflow", "WORKFLOW", "From device to live picture", (
        ("Choose a device", "Select your camera or use the", "GStreamer test pattern."),
        ("Choose a mode", "Start with Automatic or choose", "a specific advertised capture mode."),
        ("Start preview", "Check the video and read the", "capture rate shown under the picture."),
        ("Tune and apply", "Adjust a control the camera supports.", "Apply changes to write them to the device."),
    ))
    cards("states", "PREVIEW STATES", "What the preview is doing", (
        ("Stopped", "Select a camera and a capture mode.", "The device stream is closed."),
        ("Starting", "The video pipeline is opening", "and negotiating a stream."),
        ("Capturing", "The app draws the video and", "reports the measured source FPS."),
        ("Interrupted", "Read the error in Diagnostics.", "Reconnect the device and retry."),
    ))
    cards("numbers", "BY THE NUMBERS", "Supported modes and local tools", (
        ("30 / 60 / 120 FPS", "Rates provided by the synthetic test source.", "Physical modes depend on the camera."),
        ("3 appearance modes", "System, light and dark in the native app.", "The HTML design explores more themes."),
    ))
    cards("roadmap", "ROADMAP", "From preview to production", (
        ("IN SOURCE · Camera foundation", "Device selection, preview, driver", "controls and diagnostics."),
        ("NEXT · Linux validation", "Verify the desktop UI and test on", "physical cameras at advertised rates."),
        ("PLANNED · Capture tools", "Recording, overlays, effects", "and virtual camera output."),
        ("PLANNED · Distribution", "Package and verify Linux builds.", "AppImage, Debian and RPM are targets."),
    ))


if __name__ == "__main__":
    main()
