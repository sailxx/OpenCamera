"""Native GTK entry point and camera workbench."""

from concurrent.futures import ThreadPoolExecutor
import shutil
import sys

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Gdk", "4.0")
gi.require_version("Adw", "1")
gi.require_version("Gst", "1.0")
gi.require_version("GstVideo", "1.0")

from gi.repository import Adw, Gio, GLib, Gst, Gtk

from .preview import Preview
from .v4l2 import TEST_DEVICE, inspect_device, scan_devices, write_control


def label(text, *, style=None):
    item = Gtk.Label(label=text, xalign=0, wrap=True)
    if style:
        item.add_css_class(style)
    return item


def dropdown():
    return Gtk.DropDown(model=Gtk.StringList.new([]), hexpand=True, enable_search=True)


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
        self.editors = []
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

        toolbar = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        toolbar.append(Adw.HeaderBar())
        body = Gtk.Box()
        toolbar.append(body)
        self.window.set_content(toolbar)

        sidebar = Gtk.ListBox(selection_mode=Gtk.SelectionMode.SINGLE)
        sidebar.add_css_class("navigation-sidebar")
        sidebar.set_size_request(148, -1)
        body.append(sidebar)
        self.pages = Gtk.Stack(hexpand=True, vexpand=True)
        body.append(self.pages)

        self.pages.add_named(self.build_camera(), "camera")
        self.pages.add_named(self.build_diagnostics(), "diagnostics")
        self.pages.add_named(self.build_settings(), "settings")
        for name, title, icon in (
            ("camera", "Camera", "camera-photo-symbolic"),
            ("diagnostics", "Diagnostics", "dialog-information-symbolic"),
            ("settings", "Settings", "emblem-system-symbolic"),
        ):
            row = Gtk.ListBoxRow(name=name)
            entry = Gtk.Box(spacing=8, margin_top=6, margin_bottom=6, margin_start=8, margin_end=8)
            entry.append(Gtk.Image.new_from_icon_name(icon))
            entry.append(label(title))
            row.set_child(entry)
            sidebar.append(row)
        sidebar.connect("row-selected", self.navigate)
        sidebar.select_row(sidebar.get_row_at_index(0))

        self.window.present()
        if self.smoke_test:
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
        page = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=16,
                       margin_top=20, margin_bottom=20, margin_start=20, margin_end=20)
        device_group = Adw.PreferencesGroup()
        device_row = Adw.ActionRow(title="Device", subtitle="Video4Linux camera")
        self.device_select = dropdown()
        self.device_select.set_valign(Gtk.Align.CENTER)
        self.device_select.connect("notify::selected", self.device_selected)
        device_row.add_suffix(self.device_select)
        self.refresh_button = Gtk.Button(icon_name="view-refresh-symbolic", valign=Gtk.Align.CENTER)
        self.refresh_button.set_tooltip_text("Refresh cameras")
        self.refresh_button.update_property([Gtk.AccessibleProperty.LABEL], ["Refresh cameras"])
        self.refresh_button.connect("clicked", lambda _button: self.scan())
        device_row.add_suffix(self.refresh_button)
        device_group.add(device_row)
        page.append(device_group)

        self.notice = label("", style="error")
        self.notice.set_visible(False)
        page.append(self.notice)
        split = Gtk.Paned(orientation=Gtk.Orientation.HORIZONTAL, vexpand=True, wide_handle=True)
        split.set_position(700)
        split.set_resize_end_child(False)
        page.append(split)

        view = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12, hexpand=True, vexpand=True)
        view.add_css_class("card")
        view.set_size_request(280, -1)
        split.set_start_child(view)
        title = label("Preview", style="title-3")
        title.set_margin_start(16)
        title.set_margin_top(12)
        view.append(title)
        video = Gtk.Overlay(vexpand=True, margin_start=12, margin_end=12)
        self.picture = Gtk.Picture(can_shrink=True, content_fit=Gtk.ContentFit.CONTAIN)
        video.set_child(self.picture)
        self.placeholder = Adw.StatusPage(
            icon_name="camera-photo-symbolic", title="Camera inactive",
            description="Select a camera and start the preview.",
        )
        self.placeholder.set_can_target(False)
        video.add_overlay(self.placeholder)
        view.append(video)
        bottom = Gtk.Box(spacing=8, margin_start=16, margin_end=16, margin_bottom=12)
        self.status = label("Capture stopped", style="dim-label")
        self.status.set_hexpand(True)
        bottom.append(self.status)
        self.preview_button = Gtk.Button(label="Start preview", sensitive=False)
        self.preview_button.add_css_class("suggested-action")
        self.preview_button.connect("clicked", self.toggle_preview)
        bottom.append(self.preview_button)
        view.append(bottom)
        self.preview = Preview(self.picture, self.show_rate, self.preview_failed)

        controls = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=16, margin_start=8,
                           margin_end=8)
        scroller = Gtk.ScrolledWindow(hscrollbar_policy=Gtk.PolicyType.NEVER, vexpand=True)
        scroller.set_min_content_width(300)
        scroller.set_child(controls)
        split.set_end_child(scroller)
        self.mode_select = dropdown()
        self.mode_select.connect("notify::selected", self.mode_selected)
        capture_group = Adw.PreferencesGroup(
            title="Capture mode", description="Resolution, frame rate and pixel format"
        )
        capture_group.add(self.mode_select)
        controls.append(capture_group)
        self.control_group = Adw.PreferencesGroup(
            title="Image adjustments", description="Controls reported by the selected camera"
        )
        controls.append(self.control_group)
        self.apply = Gtk.Button(label="Apply changes", sensitive=False, halign=Gtk.Align.END)
        self.apply.connect("clicked", self.apply_controls)
        controls.append(self.apply)
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

    def navigate(self, _sidebar, row):
        if row:
            self.pages.set_visible_child_name(row.get_name())
            if row.get_name() == "diagnostics":
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

    def submit(self, work, completion):
        future = self.pool.submit(work)

        def deliver():
            if not self.closed:
                try:
                    result = future.result()
                except Exception as error:
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
        self.mode_select.set_model(Gtk.StringList.new([]))
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
        self.mode_select.set_model(Gtk.StringList.new(["Automatic"] + [mode.label for mode in self.modes]))
        self.mode_select.set_selected(0)
        self.show_controls(controls)
        self.set_busy(False)
        self.notify(self.device_issues[0] if self.device_issues else "")
        if self.smoke_test:
            self.mode_select.set_selected(2)
            self.toggle_preview(None)

    def mode_selected(self, *_args):
        if self.running:
            self.stop_preview()

    def show_controls(self, controls):
        for _control, row, _get_value in self.editors:
            self.control_group.remove(row)
        self.editors.clear()
        self.control_group.set_visible(bool(controls))
        self.apply.set_visible(any(control.writable for control in controls))
        for control in controls:
            if control.kind == "bool":
                row = Adw.SwitchRow(title=control.label, active=bool(control.value), sensitive=control.writable)
                row.connect("notify::active", self.controls_changed)
                read = row.get_active
            elif control.choices:
                choices = list(control.choices)
                row = Adw.ComboRow(title=control.label, sensitive=control.writable,
                                   model=Gtk.StringList.new(list(control.choices.values())))
                row.set_selected(choices.index(control.value) if control.value in choices else Gtk.INVALID_LIST_POSITION)
                row.connect("notify::selected", self.controls_changed)

                def read(row=row, choices=choices):
                    index = row.get_selected()
                    return choices[index] if index < len(choices) else None
            elif control.kind == "int":
                row = Adw.ActionRow(title=control.label, sensitive=control.writable)
                spin = Gtk.SpinButton.new_with_range(control.minimum, control.maximum, control.step)
                spin.set_valign(Gtk.Align.CENTER)
                spin.set_snap_to_ticks(True)
                spin.set_value(control.value)
                spin.connect("value-changed", self.controls_changed)
                row.add_suffix(spin)
                read = spin.get_value_as_int
            else:
                continue
            self.control_group.add(row)
            self.editors.append((control, row, read))
        self.controls_changed()

    def pending_controls(self):
        changed = []
        for control, _row, read in self.editors:
            value = read()
            if control.writable and value is not None and value != control.value:
                changed.append((control, value))
        return changed

    def controls_changed(self, *_args):
        self.apply.set_sensitive(not self.busy and bool(self.pending_controls()))

    def apply_controls(self, _button):
        device = self.selected_device()
        changes = self.pending_controls()
        if device is None or not changes:
            return
        self.set_busy(True)

        def work():
            issues = []
            for control, value in changes:
                try:
                    write_control(device, control, value)
                except (RuntimeError, ValueError) as error:
                    issues.append(f"{control.label}: {error}")
            _modes, controls, probe_issues = inspect_device(device)
            return controls, issues + probe_issues

        def finish(result):
            controls, self.device_issues = result
            self.show_controls(controls)
            self.set_busy(False)
            self.notify(self.device_issues[0] if self.device_issues else "")

        self.submit(work, finish)

    def set_busy(self, busy):
        self.busy = busy
        self.refresh_button.set_sensitive(not busy)
        self.device_select.set_sensitive(not busy and bool(self.devices))
        self.mode_select.set_sensitive(not busy and self.selected_device() is not None)
        self.control_group.set_sensitive(not busy)
        self.preview_button.set_sensitive(not busy and self.selected_device() is not None)
        self.controls_changed()

    def toggle_preview(self, _button):
        if self.running:
            self.stop_preview()
            return
        device = self.selected_device()
        if device is None:
            return
        selected = self.mode_select.get_selected()
        mode = self.modes[selected - 1] if 1 <= selected <= len(self.modes) else None
        self.preview_error = None
        self.notify("")
        try:
            self.preview.start(device, mode)
        except RuntimeError as error:
            self.preview_failed(str(error))
            return
        self.running = True
        self.status.set_text("Starting capture…")
        self.preview_button.set_label("Stop preview")
        self.preview_button.remove_css_class("suggested-action")
        self.preview_button.add_css_class("destructive-action")

    def show_rate(self, fps):
        self.placeholder.set_visible(False)
        self.status.set_text(f"Capture  ·  {fps:.1f} FPS")
        if self.smoke_test and fps > 0:
            print(f"Synthetic preview rendered at {fps:.1f} source FPS.")
            GLib.idle_add(self.finish_smoke)

    def stop_preview(self):
        self.preview.stop()
        self.running = False
        self.placeholder.set_visible(True)
        self.status.set_text("Capture stopped")
        self.preview_button.set_label("Start preview")
        self.preview_button.remove_css_class("destructive-action")
        self.preview_button.add_css_class("suggested-action")

    def preview_failed(self, message):
        self.stop_preview()
        self.preview_error = message
        self.notify(message)
        if self.smoke_test:
            GLib.idle_add(self.finish_smoke, message)

    def close_window(self, _window):
        self.closed = True
        self.preview.stop()
        self.pool.shutdown(wait=False, cancel_futures=True)
        return False
