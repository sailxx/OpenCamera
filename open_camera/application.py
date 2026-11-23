"""Native GTK entry point and camera workbench."""

from concurrent.futures import ThreadPoolExecutor
from dataclasses import replace
from pathlib import Path
import shutil
import sys

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Gdk", "4.0")
gi.require_version("Adw", "1")
gi.require_version("Gst", "1.0")
gi.require_version("GstVideo", "1.0")

from gi.repository import Adw, Gdk, Gio, GLib, Gst, Gtk, Pango

from .preview import Preview
from .v4l2 import TEST_DEVICE, apply_control_changes, inspect_device, preferred_mode, scan_devices


def label(text, *, style=None):
    item = Gtk.Label(label=text, xalign=0, wrap=True)
    if style:
        item.add_css_class(style)
    return item


ASSETS = Path(__file__).resolve().parent


def icon(name, size=16):
    file = Gio.File.new_for_path(str(ASSETS / "icons" / f"oc-{name}-symbolic.svg"))
    paintable = Gtk.IconPaintable.new_for_file(file, size, 2)
    image = Gtk.Image.new_from_paintable(paintable)
    image.set_pixel_size(size)
    return image


def accessible_name(widget, title):
    widget.update_property([Gtk.AccessibleProperty.LABEL], [title])


def dropdown(title, *, width=12, search=False):
    widget = Gtk.DropDown(model=Gtk.StringList.new([]), enable_search=search)
    accessible_name(widget, title)
    factory = Gtk.SignalListItemFactory()

    def setup(_factory, item):
        child = label("")
        child.set_wrap(False)
        child.set_ellipsize(Pango.EllipsizeMode.END)
        child.set_width_chars(width)
        item.set_child(child)

    def bind(_factory, item):
        value = item.get_item().get_string()
        item.get_child().set_text(value)
        item.get_child().set_tooltip_text(value)

    factory.connect("setup", setup)
    factory.connect("bind", bind)
    widget.set_list_factory(widget.get_factory())
    widget.set_factory(factory)
    return widget


def heading(symbol, title, subtitle):
    row = Gtk.Box(spacing=8)
    tile = icon(symbol)
    tile.add_css_class("symbol-tile")
    tile.add_css_class(f"symbol-{symbol}")
    tile.set_valign(Gtk.Align.CENTER)
    row.append(tile)
    words = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2, hexpand=True)
    words.append(label(title, style="card-title"))
    words.append(label(subtitle, style="secondary"))
    row.append(words)
    return row


def card():
    panel = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
    panel.add_css_class("workbench-card")
    return panel


def value_row(title, widget):
    row = Gtk.Box(spacing=8)
    caption = label(title)
    caption.set_hexpand(True)
    row.append(caption)
    row.append(widget)
    return row


def status_chip(text):
    row = Gtk.Box(spacing=4, valign=Gtk.Align.CENTER)
    row.add_css_class("status-chip")
    dot = Gtk.Box(valign=Gtk.Align.CENTER)
    dot.add_css_class("status-dot")
    row.append(dot)
    title = label(text)
    row.append(title)
    return row, title


class OpenCamera(Adw.Application):
    def __init__(self, use_test_source=False, *, smoke_test=False):
        super().__init__(
            application_id="io.github.sailxx.OpenCamera",
            flags=Gio.ApplicationFlags.NON_UNIQUE if use_test_source else Gio.ApplicationFlags.DEFAULT_FLAGS,
        )
        self.use_test_source = use_test_source
        self.smoke_test = smoke_test
        self.smoke_status = 1
        self.pool = ThreadPoolExecutor(max_workers=1)
        self.selection = 0
        self.closed = False
        self.devices = []
        self.modes = []
        self.sizes = []
        self.formats = []
        self.rates = []
        self.updating_modes = False
        self.editors = {}
        self.control_changes = {}
        self.updating_controls = False
        self.writing_controls = False
        self.control_timer = 0
        self.restart_timer = 0
        self.active_mode = None
        self.smoke_reconfigured = False
        self.scan_issues = []
        self.device_issues = []
        self.preview_error = None
        self.updating_devices = False
        self.busy = False
        self.running = False

    def do_activate(self):
        if self.get_active_window():
            self.get_active_window().present()
            return
        Gst.init(None)
        self.window = Adw.ApplicationWindow(application=self, title="Open Camera")
        self.window.set_default_size(1216, 780)
        self.window.connect("close-request", self.close_window)

        display = self.window.get_display()
        provider = Gtk.CssProvider()
        provider.load_from_path(str(ASSETS / "workbench.css"))
        Gtk.StyleContext.add_provider_for_display(display, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        self.window.add_css_class("open-camera")
        style = Adw.StyleManager.get_default()

        def sync_color_scheme(*_args):
            if style.get_dark():
                self.window.add_css_class("workbench-dark")
            else:
                self.window.remove_css_class("workbench-dark")

        sync_color_scheme()
        style.connect("notify::dark", sync_color_scheme)

        toolbar = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        header = Adw.HeaderBar()
        header.add_css_class("workbench-header")
        toolbar.append(header)
        body = Gtk.Box(vexpand=True)
        toolbar.append(body)
        self.window.set_content(toolbar)

        sidebar = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        sidebar.add_css_class("workbench-sidebar")
        sidebar.set_size_request(152, -1)
        body.append(sidebar)
        self.pages = Gtk.Stack(hexpand=True, vexpand=True)
        body.append(self.pages)
        self.pages.add_named(self.build_camera(), "camera")
        empty_sections = (
            ("effects", "Effects", "No effects applied", "Live effects are not available in this version."),
            ("overlays", "Overlays", "No overlays added", "Custom overlays are not available in this version."),
            ("profiles", "Profiles", "No saved profiles", "Saving camera profiles is not available in this version."),
        )
        for name, title, empty_title, description in empty_sections:
            self.pages.add_named(self.build_empty_section(name, title, empty_title, description), name)
        self.pages.add_named(self.build_diagnostics(), "diagnostics")
        self.pages.add_named(self.build_settings(), "settings")

        self.navigation = {}
        sections = (
            ("camera", "Camera"),
            *((name, title) for name, title, _, _ in empty_sections),
            ("diagnostics", "Diagnostics"),
            ("settings", "Settings"),
        )
        for name, title in sections:
            entry = Gtk.Box(spacing=8)
            entry.append(icon(name))
            text = label(title)
            text.set_hexpand(True)
            entry.append(text)
            if name == "camera":
                self.connection_dot = Gtk.Box(valign=Gtk.Align.CENTER, visible=False)
                self.connection_dot.add_css_class("connection-dot")
                entry.append(self.connection_dot)
            elif name == "settings":
                sidebar.append(Gtk.Box(vexpand=True))
            button = Gtk.Button(child=entry)
            button.add_css_class("workbench-nav")
            accessible_name(button, title)
            button.connect("clicked", lambda _button, name=name: self.navigate(name))
            self.navigation[name] = button
            sidebar.append(button)
        self.navigate("camera")

        self.window.present()
        if self.smoke_test:
            if not (ASSETS / "icons" / "oc-still-symbolic.svg").is_file():
                GLib.idle_add(self.finish_smoke, "The viewfinder's symbolic icon is missing.")
                return
            for name, *_ in empty_sections:
                self.navigation[name].emit("clicked")
                if self.pages.get_visible_child_name() != name:
                    GLib.idle_add(self.finish_smoke, f"Could not open the {name} section.")
                    return
            self.navigation["camera"].emit("clicked")
            GLib.timeout_add_seconds(20, self.finish_smoke, "Timed out waiting for synthetic frames.")
        self.scan()

    def run(self, argv):
        status = super().run(argv)
        return self.smoke_status if self.smoke_test else status

    def finish_smoke(self, error=None):
        if error:
            print(error, file=sys.stderr)
        else:
            self.smoke_status = 0
        self.window.close()
        return GLib.SOURCE_REMOVE

    def build_camera(self):
        page = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8,
                       margin_top=12, margin_bottom=12, margin_start=24, margin_end=24)
        self.notice = label("", style="workbench-notice")
        self.notice.set_visible(False)
        page.append(self.notice)

        workspace = Gtk.Box(spacing=24, vexpand=True)
        page.append(workspace)
        left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=16, hexpand=True)
        left.set_size_request(380, -1)
        workspace.append(left)

        device = card()
        device.add_css_class("device-card")
        device_row = Gtk.Box(spacing=8)
        device_row.append(heading("camera", "Device", "Select a source for the preview"))
        self.device_select = dropdown("Device", width=16, search=True)
        self.device_select.set_valign(Gtk.Align.CENTER)
        self.device_select.connect("notify::selected", self.device_selected)
        device_row.append(self.device_select)
        self.refresh_button = Gtk.Button(child=icon("refresh"), valign=Gtk.Align.CENTER)
        self.refresh_button.add_css_class("refresh-button")
        self.refresh_button.set_tooltip_text("Refresh cameras")
        accessible_name(self.refresh_button, "Refresh cameras")
        self.refresh_button.connect("clicked", lambda _button: self.scan())
        device_row.append(self.refresh_button)
        device.append(device_row)
        left.append(device)
        left.append(self.build_preview())

        controls = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=16)
        scroller = Gtk.ScrolledWindow(hscrollbar_policy=Gtk.PolicyType.NEVER,
                                      vscrollbar_policy=Gtk.PolicyType.EXTERNAL, vexpand=True)
        scroller.set_min_content_width(312)
        accessible_name(scroller, "Camera controls")
        scroller.set_child(controls)
        workspace.append(scroller)
        controls.append(self.build_capture_modes())

        image = card()
        image.append(heading("image", "Image adjustments", "Adjust the camera image"))
        image.append(Gtk.Separator())
        self.control_group = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.no_controls = label("No image controls reported.", style="secondary")
        image.append(self.no_controls)
        image.append(self.control_group)
        reset_content = Gtk.Box(spacing=4)
        reset_content.append(icon("undo"))
        reset_content.append(label("Reset controls"))
        self.reset = Gtk.Button(child=reset_content, halign=Gtk.Align.START)
        self.reset.add_css_class("flat")
        self.reset.set_tooltip_text("Restore the camera’s factory defaults")
        self.reset.connect("clicked", self.reset_controls)
        image.append(self.reset)
        controls.append(image)

        info = card()
        info.append(heading("info", "Device info", "Connection details"))
        info.append(Gtk.Separator())
        self.device_state, self.device_status = status_chip("Disconnected")
        self.device_state.set_halign(Gtk.Align.START)
        info.append(self.device_state)
        self.device_path = label("—", style="secondary")
        info.append(value_row("Device ID", self.device_path))
        controls.append(info)
        return page

    def build_preview(self):
        view = card()
        view.set_vexpand(True)
        top = Gtk.Box(spacing=8)
        top.append(heading("preview", "Preview", "Camera viewfinder"))
        self.live_chip, self.live_status = status_chip("Paused")
        top.append(self.live_chip)
        view.append(top)

        video = Gtk.Overlay(vexpand=True, overflow=Gtk.Overflow.HIDDEN)
        video.add_css_class("viewfinder")
        video.set_size_request(-1, 256)
        texture = Gdk.Texture.new_from_filename(str(ASSETS / "workbench-scene.jpg"))
        self.scene = Gtk.Picture(paintable=texture, can_shrink=True, content_fit=Gtk.ContentFit.COVER)
        self.scene.add_css_class("idle-scene")
        video.set_child(self.scene)
        self.picture = Gtk.Picture(can_shrink=True, content_fit=Gtk.ContentFit.CONTAIN)
        video.add_overlay(self.picture)

        self.placeholder = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12,
                                   halign=Gtk.Align.CENTER, valign=Gtk.Align.CENTER)
        self.placeholder.add_css_class("idle-panel")
        camera = icon("still", 36)
        camera.add_css_class("idle-camera")
        self.placeholder.append(camera)
        title = label("Camera inactive", style="idle-title")
        title.set_halign(Gtk.Align.CENTER)
        self.placeholder.append(title)
        self.preview_hint = label("Start the preview to frame your shot.", style="idle-hint")
        self.preview_hint.set_halign(Gtk.Align.CENTER)
        self.placeholder.append(self.preview_hint)
        self.preview_button = Gtk.Button(label="Start preview", sensitive=False, halign=Gtk.Align.CENTER)
        self.preview_button.add_css_class("start-preview")
        self.preview_button.connect("clicked", self.toggle_preview)
        self.placeholder.append(self.preview_button)
        video.add_overlay(self.placeholder)

        self.stop_button = Gtk.Button(label="Stop preview", halign=Gtk.Align.END, valign=Gtk.Align.START,
                                      margin_top=16, margin_end=16, visible=False)
        self.stop_button.add_css_class("stop-preview")
        self.stop_button.connect("clicked", self.toggle_preview)
        video.add_overlay(self.stop_button)
        view.append(video)

        self.capture_chip, self.status = status_chip("Capture stopped")
        self.capture_chip.set_halign(Gtk.Align.START)
        view.append(self.capture_chip)
        meter = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        meter.add_css_class("fps-meter")
        self.rate_readout = label("—")
        meter.append(value_row("Measured FPS / selected FPS", self.rate_readout))
        segments = Gtk.Box(spacing=2, homogeneous=True)
        self.rate_segments = []
        for _ in range(20):
            segment = Gtk.Box()
            segment.add_css_class("fps-segment")
            self.rate_segments.append(segment)
            segments.append(segment)
        meter.append(segments)
        view.append(meter)

        self.preview = Preview(self.picture, self.show_rate, self.preview_failed)
        return view

    def build_capture_modes(self):
        capture = card()
        capture.append(heading("capture", "Capture mode", "Available modes for this device"))
        capture.append(Gtk.Separator())
        self.size_select = dropdown("Resolution")
        capture.append(value_row("Resolution", self.size_select))
        self.format_select = dropdown("Format", width=6)
        capture.append(value_row("Format", self.format_select))

        self.fps_value = label("—", style="secondary")
        capture.append(value_row("Frame rate", self.fps_value))
        self.fps_scale = Gtk.Scale.new_with_range(Gtk.Orientation.HORIZONTAL, 0, 1, 1)
        self.fps_scale.set_draw_value(False)
        self.fps_scale.add_css_class("capture-slider")
        accessible_name(self.fps_scale, "Frame rate")
        capture.append(self.fps_scale)
        self.mode_badge = label("Automatic negotiation", style="mode-badge")
        self.mode_badge.set_halign(Gtk.Align.START)
        capture.append(self.mode_badge)
        self.size_select.connect("notify::selected", self.update_formats)
        self.format_select.connect("notify::selected", self.update_rates)
        self.fps_scale.connect("value-changed", self.rate_selected)
        return capture

    def build_empty_section(self, name, title, empty_title, description):
        page = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=16,
                       margin_top=24, margin_bottom=24, margin_start=24, margin_end=24)
        page.append(label(title, style="title-1"))

        panel = card()
        panel.add_css_class("empty-section")
        symbol = icon(name, 24)
        symbol.add_css_class("symbol-tile")
        symbol.set_halign(Gtk.Align.CENTER)
        panel.append(symbol)
        message = label(empty_title, style="card-title")
        message.set_halign(Gtk.Align.CENTER)
        panel.append(message)
        detail = label(description, style="secondary")
        detail.set_justify(Gtk.Justification.CENTER)
        detail.set_halign(Gtk.Align.CENTER)
        panel.append(detail)

        back = Gtk.Button(label="Back to camera", halign=Gtk.Align.CENTER)
        back.add_css_class("flat")
        back.connect("clicked", lambda _button: self.navigate("camera"))
        panel.append(back)
        page.append(panel)
        return page

    def build_diagnostics(self):
        page = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12,
                       margin_top=24, margin_start=24, margin_end=24, margin_bottom=24)
        page.append(label("Diagnostics", style="title-1"))
        self.diagnostic_text = label("")
        self.diagnostic_text.set_selectable(True)
        page.append(self.diagnostic_text)
        scroll = Gtk.ScrolledWindow(hscrollbar_policy=Gtk.PolicyType.NEVER)
        scroll.set_child(page)
        return scroll

    def build_settings(self):
        page = Adw.PreferencesPage()
        group = Adw.PreferencesGroup(title="Appearance")
        row = Adw.ComboRow(title="Color scheme", model=Gtk.StringList.new(["System", "Light", "Dark"]))
        schemes = (Adw.ColorScheme.DEFAULT, Adw.ColorScheme.FORCE_LIGHT, Adw.ColorScheme.FORCE_DARK)
        row.connect("notify::selected", lambda widget, _prop: Adw.StyleManager.get_default().set_color_scheme(
            schemes[widget.get_selected()]
        ))
        group.add(row)
        page.add(group)
        return page

    def navigate(self, name):
        self.pages.set_visible_child_name(name)
        for page, button in self.navigation.items():
            if page == name:
                button.add_css_class("selected")
            else:
                button.remove_css_class("selected")
        if name == "diagnostics":
            self.update_diagnostics()

    def diagnostics(self):
        elements = ["v4l2src", "decodebin", "videoconvert", "appsink", "gtk4paintablesink"]
        report = ["v4l2-ctl: " + ("available" if shutil.which("v4l2-ctl") else "missing")]
        for name in elements:
            available = Gst.ElementFactory.find(name) is not None
            label_when_missing = "optional — texture fallback" if name == "gtk4paintablesink" else "missing"
            report.append(f"{name}: {'available' if available else label_when_missing}")
        report.append(f"Cameras discovered: {sum(not device.test for device in self.devices)}")
        report.extend(self.scan_issues + self.device_issues)
        if self.preview_error:
            report.append(self.preview_error)
        return "\n".join(report)

    def update_diagnostics(self):
        self.diagnostic_text.set_text(self.diagnostics())

    def notify(self, message=""):
        self.notice.set_text(message)
        self.notice.set_visible(bool(message))
        self.update_diagnostics()

    def submit(self, work, completion, on_error=None):
        future = self.pool.submit(work)

        def deliver():
            if not self.closed:
                try:
                    result = future.result()
                except Exception as error:
                    if on_error:
                        on_error(error)
                    else:
                        self.set_busy(False)
                        self.notify(str(error))
                else:
                    completion(result)
            return GLib.SOURCE_REMOVE

        future.add_done_callback(lambda _done: GLib.idle_add(deliver))

    def scan(self):
        self.stop_preview()
        self.selection += 1
        selected = self.selected_device()
        self.set_busy(True)
        self.notify("")
        self.submit(scan_devices, lambda result: self.show_devices(result, selected))

    def show_devices(self, result, selected):
        devices, self.scan_issues = result
        if self.use_test_source:
            devices.append(TEST_DEVICE)
        self.updating_devices = True
        self.devices = devices
        self.device_select.set_model(Gtk.StringList.new([device.label for device in devices]))
        if selected in devices:
            self.device_select.set_selected(devices.index(selected))
        elif self.use_test_source:
            self.device_select.set_selected(devices.index(TEST_DEVICE))
        elif devices:
            self.device_select.set_selected(0)
        self.updating_devices = False
        self.device_selected()

    def selected_device(self):
        index = self.device_select.get_selected()
        return self.devices[index] if index < len(self.devices) else None

    def device_selected(self, *_args):
        if self.updating_devices:
            return
        self.selection += 1
        request = self.selection
        device = self.selected_device()
        self.stop_preview()
        self.preview_error = None
        self.device_issues = []
        self.modes = []
        self.configure_modes()
        self.connection_dot.set_visible(device is not None)
        self.device_status.set_text("Connected" if device else "Disconnected")
        self.device_path.set_text(device.path if device and device.path else "—")
        if device:
            self.device_state.add_css_class("connected")
        else:
            self.device_state.remove_css_class("connected")
        self.show_controls([])
        if device is None:
            self.set_busy(False)
            self.notify("No camera found. Check the connection or open Diagnostics.")
            return
        self.set_busy(True)
        self.notify("")
        self.submit(lambda: inspect_device(device), lambda result: self.show_device(result, request))

    def show_device(self, result, request):
        if request != self.selection:
            return
        self.modes, controls, self.device_issues = result
        initial_mode = preferred_mode(self.modes, require_60=True)
        self.configure_modes(initial_mode)
        self.show_controls(controls)
        self.set_busy(False)
        self.notify(self.device_issues[0] if self.device_issues else "")
        if self.smoke_test:
            if self.selected_mode() is None or self.selected_mode().fps != 60:
                self.finish_smoke("The capture controls did not select the 60 FPS mode.")
                return
            self.toggle_preview(None)

    def configure_modes(self, initial_mode=None):
        self.sizes = sorted({(mode.width, mode.height) for mode in self.modes}, reverse=True)
        self.updating_modes = True
        self.size_select.set_model(Gtk.StringList.new(
            ["Automatic"] + [f"{width} × {height}" for width, height in self.sizes]
        ))
        size = (initial_mode.width, initial_mode.height) if initial_mode else None
        self.size_select.set_selected(self.sizes.index(size) + 1 if size else 0)
        self.updating_modes = False
        self.update_formats()

    def update_formats(self, *_args):
        if self.updating_modes:
            return
        index = self.size_select.get_selected()
        size = self.sizes[index - 1] if 1 <= index <= len(self.sizes) else None
        self.resolution_modes = [mode for mode in self.modes if (mode.width, mode.height) == size]
        self.formats = sorted({mode.fourcc for mode in self.resolution_modes})
        self.updating_modes = True
        self.format_select.set_model(Gtk.StringList.new(self.formats or ["Automatic"]))
        preferred = preferred_mode(self.resolution_modes)
        self.format_select.set_selected(self.formats.index(preferred.fourcc) if preferred else 0)
        self.updating_modes = False
        self.update_rates()

    def update_rates(self, *_args):
        if self.updating_modes:
            return
        index = self.format_select.get_selected()
        self.rates = sorted(
            (mode for mode in self.resolution_modes if index < len(self.formats)
             and mode.fourcc == self.formats[index]),
            key=lambda mode: mode.fps,
        )
        self.updating_modes = True
        self.fps_scale.set_range(0, max(1, len(self.rates) - 1))
        preferred = preferred_mode(self.rates)
        self.fps_scale.set_value(self.rates.index(preferred) if preferred else 0)
        self.updating_modes = False
        self.refresh_mode_sensitivity()
        supported = self.rates
        if not self.resolution_modes:
            supported = self.modes
        rates = sorted({mode.fps for mode in supported})
        if rates:
            shown = " / ".join(self.format_rate(rate) for rate in rates[:3])
            if len(rates) > 3:
                shown += " / …"
            self.mode_badge.set_text(f"Supported {shown} FPS")
            self.mode_badge.set_tooltip_text(", ".join(self.format_rate(rate) for rate in rates) + " FPS")
        else:
            self.mode_badge.set_text("Automatic negotiation")
            self.mode_badge.set_tooltip_text(None)
        self.rate_selected()

    @staticmethod
    def format_rate(rate):
        return f"{float(rate):.3f}".rstrip("0").rstrip(".")

    def selected_mode(self):
        index = round(self.fps_scale.get_value())
        return self.rates[index] if index < len(self.rates) else None

    def rate_selected(self, *_args):
        if self.updating_modes:
            return
        mode = self.selected_mode()
        self.fps_value.set_text(f"{self.format_rate(mode.fps)} FPS" if mode else "Automatic")
        if self.running:
            self.schedule_preview_restart()
        else:
            self.update_meter()

    def schedule_preview_restart(self):
        if self.restart_timer:
            GLib.source_remove(self.restart_timer)
            self.restart_timer = 0
        if self.running and self.active_mode != self.selected_mode() and not self.writing_controls:
            self.restart_timer = GLib.timeout_add(150, self.restart_preview)

    def restart_preview(self):
        self.restart_timer = 0
        if self.running and not self.writing_controls:
            self.start_preview()
        return GLib.SOURCE_REMOVE

    def refresh_mode_sensitivity(self):
        self.size_select.set_sensitive(not self.busy and bool(self.sizes))
        self.format_select.set_sensitive(not self.busy and len(self.formats) > 1)
        self.fps_scale.set_sensitive(not self.busy and len(self.rates) > 1)

    def show_controls(self, controls):
        for _control, row, _read, _write in self.editors.values():
            self.control_group.remove(row)
        self.editors.clear()
        for control in controls:
            if control.kind == "bool":
                switch = Gtk.Switch(active=bool(control.value), valign=Gtk.Align.CENTER)
                accessible_name(switch, control.label)
                switch.connect("notify::active", lambda *_args, name=control.name: self.queue_control(name))
                row = value_row(control.label, switch)
                read = switch.get_active
                write = switch.set_active
            elif control.choices:
                choices = list(control.choices)
                picker = dropdown(control.label, width=8)
                picker.set_model(Gtk.StringList.new(list(control.choices.values())))
                picker.set_selected(choices.index(control.value) if control.value in choices else Gtk.INVALID_LIST_POSITION)
                picker.connect("notify::selected", lambda *_args, name=control.name: self.queue_control(name))
                row = value_row(control.label, picker)

                def read(picker=picker, choices=choices):
                    index = picker.get_selected()
                    return choices[index] if index < len(choices) else None

                def write(value, picker=picker, choices=choices):
                    if value in choices:
                        picker.set_selected(choices.index(value))
            elif control.kind == "int" and control.minimum + control.step <= control.maximum:
                # Use integer positions so only values valid for the driver's step can be saved.
                steps = (control.maximum - control.minimum) // control.step
                scale = Gtk.Scale.new_with_range(Gtk.Orientation.HORIZONTAL, 0, steps, 1)
                scale.set_draw_value(False)
                scale.set_digits(0)
                scale.add_css_class("capture-slider")
                accessible_name(scale, control.label)
                value = label(str(control.value), style="secondary")
                row = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
                row.append(value_row(control.label, value))
                row.append(scale)

                def read(scale=scale, control=control):
                    return control.minimum + round(scale.get_value()) * control.step

                def write(value, scale=scale, control=control):
                    scale.set_value((value - control.minimum) // control.step)

                def update_value(_scale, value=value, read=read, name=control.name):
                    value.set_text(str(read()))
                    self.queue_control(name)

                write(control.value)
                scale.connect("value-changed", update_value)
            elif control.kind == "int":
                value = label(str(control.value), style="secondary")
                row = value_row(control.label, value)
                read = lambda value=value: int(value.get_text())
                write = lambda current, value=value: value.set_text(str(current))
            else:
                continue
            row.add_css_class("control-row")
            row.set_sensitive(control.writable)
            self.control_group.append(row)
            self.editors[control.name] = (control, row, read, write)
        self.no_controls.set_visible(not self.editors)
        self.update_reset_visibility()

    def update_reset_visibility(self):
        self.reset.set_visible(any(
            control.writable and control.default is not None and
            (control.kind != "int" or control.minimum + control.step <= control.maximum)
            for control, _row, _read, _write in self.editors.values()
        ))

    def reset_controls(self, _button):
        for control, _row, read, write in self.editors.values():
            if (control.writable and control.default is not None and read() != control.default
                    and (control.kind != "int" or control.minimum + control.step <= control.maximum)):
                write(control.default)

    def queue_control(self, name):
        if self.updating_controls or self.busy:
            return
        control, _row, read, _write = self.editors[name]
        value = read()
        if control.writable and value is not None:
            self.control_changes[name] = value
            self.refresh_device_sensitivity()
            self.schedule_control_write()

    def schedule_control_write(self):
        if self.control_changes and not (self.writing_controls or self.control_timer):
            # Keep dragging responsive and collapse intermediate slider positions.
            self.control_timer = GLib.timeout_add(75, self.flush_controls)

    def flush_controls(self):
        self.control_timer = 0
        device = self.selected_device()
        if device is None or not self.control_changes:
            return GLib.SOURCE_REMOVE
        controls = [editor[0] for editor in self.editors.values()]
        changes, self.control_changes = self.control_changes, {}
        self.writing_controls = True
        self.refresh_device_sensitivity()
        self.submit(lambda: apply_control_changes(device, controls, changes), self.finish_controls,
                    lambda error: self.finish_controls((controls, [str(error)])))
        return GLib.SOURCE_REMOVE

    @staticmethod
    def editor_shape(control):
        return replace(control, flags=frozenset(), value=0, default=None)

    def finish_controls(self, result):
        self.writing_controls = False
        controls, self.device_issues = result
        controls = [control for control in controls if control.kind in {"bool", "int"} or control.choices]
        actual = {control.name: control for control in controls}
        self.updating_controls = True
        for name in tuple(self.control_changes):
            if name not in actual or not actual[name].writable:
                del self.control_changes[name]
        shapes = [self.editor_shape(control) for control in controls]
        if shapes != [self.editor_shape(editor[0]) for editor in self.editors.values()]:
            self.show_controls(controls)
        for name, (_control, row, read, write) in self.editors.items():
            reported = actual[name]
            value = self.control_changes.get(name, reported.value)
            if read() != value:
                write(value)
            row.set_sensitive(reported.writable)
            self.editors[name] = (reported, row, read, write)
        self.update_reset_visibility()
        self.updating_controls = False
        self.notify(self.device_issues[0] if self.device_issues else "")
        self.refresh_device_sensitivity()
        self.schedule_preview_restart()
        self.schedule_control_write()

    def refresh_device_sensitivity(self):
        available = not (self.busy or self.writing_controls or self.control_changes)
        self.refresh_button.set_sensitive(available)
        self.device_select.set_sensitive(available and bool(self.devices))

    def set_busy(self, busy):
        self.busy = busy
        has_device = self.selected_device() is not None
        self.refresh_device_sensitivity()
        self.refresh_mode_sensitivity()
        self.control_group.set_sensitive(not busy)
        self.reset.set_sensitive(not busy)
        self.preview_button.set_sensitive(not busy and has_device)
        self.preview_hint.set_text("Checking the camera…" if busy else
                                   "Start the preview to frame your shot." if has_device else
                                   "Connect a camera to start the preview.")

    def toggle_preview(self, _button):
        if self.running:
            self.stop_preview()
            self.preview_button.grab_focus()
            return
        self.start_preview()
        if self.running:
            self.stop_button.grab_focus()

    def start_preview(self):
        device = self.selected_device()
        if device is None or self.busy:
            return
        mode = self.selected_mode()
        self.preview_error = None
        self.notify(self.device_issues[0] if self.device_issues else "")
        try:
            self.preview.start(device, mode)
        except RuntimeError as error:
            self.preview_failed(str(error))
            return
        self.running = True
        self.active_mode = mode
        self.live_chip.remove_css_class("live")
        self.capture_chip.remove_css_class("live")
        self.update_meter()
        self.scene.set_visible(False)
        self.placeholder.set_visible(False)
        self.stop_button.set_visible(True)
        self.status.set_text("Starting capture…")
        self.live_status.set_text("Starting")

    def update_meter(self, fps=0):
        mode = self.active_mode if self.running else self.selected_mode()
        target = float(mode.fps) if mode else 0
        active_segments = round(min(1, fps / target) * len(self.rate_segments)) if target else 0
        for index, segment in enumerate(self.rate_segments):
            if index < active_segments:
                segment.add_css_class("filled")
            else:
                segment.remove_css_class("filled")
        target_label = self.format_rate(mode.fps) if mode else "Auto"
        measured = f"{fps:.1f}" if fps else "0"
        self.rate_readout.set_text(f"{measured} / {target_label}")

    def show_rate(self, fps):
        self.live_status.set_text("Playing")
        self.live_chip.add_css_class("live")
        self.capture_chip.add_css_class("live")
        self.status.set_text(f"Capture active  ·  {fps:.1f} FPS")
        self.update_meter(fps)
        if self.smoke_test and fps > 0:
            print(f"Synthetic preview rendered at {fps:.1f} source FPS.")
            if not self.smoke_reconfigured:
                self.smoke_reconfigured = True
                self.fps_scale.set_value(0)
                return
            if self.active_mode and self.active_mode.fps == 30:
                GLib.idle_add(self.finish_smoke)

    def stop_preview(self):
        if self.restart_timer:
            GLib.source_remove(self.restart_timer)
            self.restart_timer = 0
        self.preview.stop()
        self.running = False
        self.active_mode = None
        self.scene.set_visible(True)
        self.placeholder.set_visible(True)
        self.stop_button.set_visible(False)
        self.live_status.set_text("Paused")
        self.live_chip.remove_css_class("live")
        self.capture_chip.remove_css_class("live")
        self.status.set_text("Capture stopped")
        self.update_meter()

    def preview_failed(self, message):
        self.stop_preview()
        self.preview_error = message
        self.notify(message)
        if self.smoke_test:
            GLib.idle_add(self.finish_smoke, message)

    def close_window(self, _window):
        self.closed = True
        if self.control_timer:
            GLib.source_remove(self.control_timer)
        self.stop_preview()
        self.pool.shutdown(wait=False, cancel_futures=True)
        return False
