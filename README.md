<div align="center">

<img src="design/open-camera.png" width="104" alt="Open Camera">

# Open Camera

**English** · [Русский](README.ru.md) · [Deutsch](README.de.md)

**A native Linux workbench for Video4Linux cameras.**

Select a webcam, see its live preview, choose a capture mode and adjust the controls exposed by the camera driver.

<img src="https://img.shields.io/badge/status-early%20development-2E9BFF" alt="Status: early development">
<img src="https://img.shields.io/badge/platform-Linux-2E9BFF" alt="Linux">
<img src="https://img.shields.io/badge/UI-GTK%204%20%7C%20libadwaita-2E9BFF" alt="GTK 4 and libadwaita">
<img src="https://img.shields.io/badge/video-GStreamer%20%7C%20V4L2-2E9BFF" alt="GStreamer and V4L2">

<br>

<img src="assets/readme/hero.svg" width="100%" alt="Open Camera, a native Linux camera workbench. The image shows the interactive design prototype.">

<a href="#run-on-linux"><img src="assets/readme/btn-linux.svg" height="48" alt="Run on Linux"></a>&nbsp;&nbsp;<a href="#design"><img src="assets/readme/btn-design.svg" height="48" alt="View the design"></a>&nbsp;&nbsp;<a href="#roadmap"><img src="assets/readme/btn-roadmap.svg" height="48" alt="See the roadmap"></a>

</div>

<br>

<img src="assets/readme/features.svg" width="100%" alt="Camera discovery, live preview, capture modes, hardware controls, diagnostics, and appearance">

<details>
<summary><b>More about the features</b></summary>

- **Cameras.** Select a V4L2 device and rescan after connecting or disconnecting a camera.
- **Live preview.** Start and stop a local stream and see the capture rate measured at the source. When available, the app paints frames with the GStreamer GTK 4 sink. It also supports a bounded GTK texture fallback.
- **Capture modes.** Use automatic negotiation or choose an advertised combination of resolution, pixel format and frame rate. Change modes between preview sessions.
- **Hardware controls.** Edit the numeric, switch and menu controls reported by the driver. **Apply changes** writes the values and reads the device back.
- **Diagnostics and appearance.** Inspect device access, missing dependencies and preview errors. Settings offers system, light and dark appearance.

</details>

<br>

<img src="assets/readme/workflow.svg" width="100%" alt="Choose a device and mode, start the preview, then adjust supported camera controls">

<br>

<img src="assets/readme/states.svg" width="100%" alt="Preview states: stopped, starting, capturing, and interrupted">

<br>

<img src="assets/readme/numbers.svg" width="100%" alt="Synthetic test pattern at 30, 60 or 120 FPS, plus three native appearance modes">

## Quick start

1. Connect a webcam and select it in **Device**. Use the refresh button if it was plugged in after opening the app.
2. Leave the capture mode on **Automatic** for the first run. To request 60 FPS or higher, choose a mode that lists that rate at the desired resolution and format.
3. Click **Start preview**. The FPS readout measures frames arriving from the source. It can differ from the requested rate and does not measure monitor refresh.
4. Adjust the controls your driver exposes. **Apply changes** writes the selected values and reads them back.

Open Camera provides a local workbench for configuring and testing a webcam. Version 0.1.0 has no recording, effects processing or virtual camera output.

<h2 id="roadmap">Roadmap</h2>

<img src="assets/readme/roadmap.svg" width="100%" alt="Camera foundation, Linux validation, capture tools, and AppImage, Debian and RPM packaging">

| Stage | Work |
| --- | --- |
| **Available · v0.1.0** | Camera selection, live preview, source FPS, driver controls, diagnostics and three Linux packages. |
| **Next · Hardware and reliability** | Validate USB and built-in cameras, check advertised 60+ FPS modes on hardware, and test recovery when a device is busy or unplugged. |
| **Planned · Capture workflow** | Add photo and video capture, overlays and effects, then explore profiles and virtual camera output. |

The roadmap sets priorities without target dates.

<h2 id="run-on-linux">📦 Run on Linux</h2>

Download Open Camera **v0.1.0** from [GitHub Releases](https://github.com/sailxx/OpenCamera/releases/tag/v0.1.0).

| Download | Install or launch |
| --- | --- |
| [DEB](https://github.com/sailxx/OpenCamera/releases/download/v0.1.0/open-camera_0.1.0_all.deb) | `sudo apt install ./open-camera_0.1.0_all.deb` on Ubuntu 24.04 |
| [RPM](https://github.com/sailxx/OpenCamera/releases/download/v0.1.0/open-camera-0.1.0-1.fc44.noarch.rpm) | `sudo dnf install ./open-camera-0.1.0-1.fc44.noarch.rpm` on Fedora 44 |
| [AppImage](https://github.com/sailxx/OpenCamera/releases/download/v0.1.0/OpenCamera-0.1.0-x86_64.AppImage) | `chmod +x OpenCamera-0.1.0-x86_64.AppImage` then `./OpenCamera-0.1.0-x86_64.AppImage` on x86_64 Linux with glibc 2.39 or newer |

Start the DEB or RPM installation from the desktop launcher or with `open-camera`. If FUSE is unavailable, launch the AppImage with `./OpenCamera-0.1.0-x86_64.AppImage --appimage-extract-and-run`.

To check the download, save [SHA256SUMS](https://github.com/sailxx/OpenCamera/releases/download/v0.1.0/SHA256SUMS) beside the package and run `sha256sum -c --ignore-missing SHA256SUMS` from that directory.

The release workflow installed or launched all three packages and checked live preview using a synthetic source. Physical webcam compatibility still needs validation.

### Run from source

Use a Linux desktop with Python 3.10+, GTK 4.8+, libadwaita 1.4+ and GStreamer 1.20+. Run from the repository folder with the system Python so it can find the distribution's PyGObject bindings.

<details open>
<summary><b>Ubuntu 24.04 and newer</b></summary>

```sh
sudo apt install python3-gi gir1.2-gtk-4.0 gir1.2-adw-1 \
  gir1.2-gstreamer-1.0 gir1.2-gst-plugins-base-1.0 \
  gstreamer1.0-plugins-base gstreamer1.0-plugins-good v4l-utils
python3 -m open_camera
```

</details>

<details>
<summary><b>Fedora</b></summary>

```sh
sudo dnf install python3-gobject gtk4 libadwaita gstreamer1 \
  gstreamer1-plugins-base gstreamer1-plugins-good v4l-utils
python3 -m open_camera
```

</details>

<details>
<summary><b>Test without a physical camera</b></summary>

```sh
python3 -m open_camera --test-source
```

For a DEB or RPM installation use `open-camera --test-source`. Select **GStreamer test pattern**, choose 30, 60 or 120 FPS at 1280 × 720 and click **Start preview**. These rates describe the test source. Physical-device modes depend on the camera and driver.

</details>

### Troubleshooting

| Symptom | What to check |
| --- | --- |
| The camera is missing | Reconnect it, refresh the device list and check **Diagnostics** for missing components or device permissions. |
| Preview fails to start | Close apps using the camera, try **Automatic**, then check **Diagnostics** for the pipeline error. Encoded modes may require an installed decoder. |
| The source FPS is below the chosen rate | Check the available rates at that resolution and format. Try a lower resolution or a different USB port and compare the measurement. |

When reporting a problem, include the distribution, camera model, selected capture mode and relevant text from **Diagnostics**.

<h2 id="design">Design</h2>

The banner shows the **interactive browser prototype**. It includes simulated frames, effects and virtual output so the interface can be explored independently of camera hardware. Download the [self-contained HTML prototype](design/open-camera-interface-options.html) and open it in a browser. The [theme stylesheet](design/open-camera-themes.css) is available separately.

<details>
<summary><b>Development and verification</b></summary>

| Path | Purpose |
| --- | --- |
| [open_camera/](open_camera/) | GTK interface, GStreamer preview and V4L2 controls |
| [tests/](tests/) | Tests for V4L2 parsing and control validation |
| [design/](design/) | Interactive prototype, themes, icon and screenshots |
| [assets/readme/](assets/readme/) | README cards and navigation buttons |

```sh
python3 -m unittest discover -s tests -v
```

On a Linux desktop, verify start and stop with the test pattern at 30 and 60 FPS. With a physical camera, check the advertised modes, the measured rate, changes to driver controls and disconnect behavior.

To regenerate the README panels, install Pillow in your development environment and run:

```sh
python3 tools/build_readme_assets.py
```

</details>

## About the author

<a href="https://github.com/sailxx"><img src="assets/readme/author.svg" width="100%" alt="sailxx on GitHub"></a>

**sailxx** is the creator of Open Camera and [Tobi](https://github.com/sailxx/Tobi), the project that inspired this README's visual style. Other projects are available on the [GitHub profile](https://github.com/sailxx).
