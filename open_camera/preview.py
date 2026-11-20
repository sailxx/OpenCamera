"""GStreamer preview, with a bounded GTK texture fallback."""

from threading import Lock
from time import monotonic

from gi.repository import Gdk, GLib, Gst, GstVideo


class Preview:
    def __init__(self, picture, on_rate, on_error):
        self.picture = picture
        self.on_rate = on_rate
        self.on_error = on_error
        self.pipeline = None
        self.bus = None
        self.bus_handler = 0
        self.poll_id = 0
        self.sink = None
        self.copy_frames = False
        self.frames = 0
        self.frame_lock = Lock()

    def start(self, device, mode):
        self.stop()
        source = "videotestsrc is-live=true" if device.test else "v4l2src"
        self.copy_frames = Gst.ElementFactory.find("gtk4paintablesink") is None
        sink = ("videoconvert ! video/x-raw,format=RGBA ! "
                "appsink name=display max-buffers=1 drop=true sync=false wait-on-eos=false"
                if self.copy_frames else "gtk4paintablesink name=display sync=false")
        # The pipeline description is static. Device paths and mode settings are properties.
        try:
            self.pipeline = Gst.parse_launch(
                f"{source} name=camera ! capsfilter name=capture ! decodebin ! "
                f"queue max-size-buffers=2 max-size-bytes=0 max-size-time=0 "
                f"leaky=downstream ! {sink}"
            )
            camera = self.pipeline.get_by_name("camera")
            if not device.test:
                camera.set_property("device", device.path)
            if mode:
                self.pipeline.get_by_name("capture").set_property("caps", Gst.Caps.from_string(mode.caps))
            self.sink = self.pipeline.get_by_name("display")
            if not self.copy_frames:
                self.picture.set_paintable(self.sink.get_property("paintable"))
            self.pipeline.get_by_name("capture").get_static_pad("src").add_probe(
                Gst.PadProbeType.BUFFER, self.count_frame
            )
            self.bus = self.pipeline.get_bus()
            self.bus.add_signal_watch()
            self.bus_handler = self.bus.connect("message", self.bus_message)
            self.frames = 0
            self.frame_mark = 0
            self.started = self.tick = monotonic()
            self.last_frame = self.started
            self.ready = False
            if self.pipeline.set_state(Gst.State.PLAYING) == Gst.StateChangeReturn.FAILURE:
                raise RuntimeError("Could not start the camera.")
            self.poll_id = GLib.timeout_add(12 if self.copy_frames else 200, self.refresh)
        except (GLib.Error, RuntimeError, TypeError) as error:
            self.stop()
            raise RuntimeError(str(error)) from error

    def count_frame(self, _pad, _probe):
        with self.frame_lock:
            self.frames += 1
        return Gst.PadProbeReturn.OK

    def refresh(self):
        if self.copy_frames:
            sample = self.sink.emit("try-pull-sample", 0)
            if sample is not None:
                try:
                    self.draw(sample)
                except (GLib.Error, RuntimeError, TypeError, ValueError) as error:
                    self.poll_id = 0
                    self.fail(str(error))
                    return GLib.SOURCE_REMOVE
                self.ready = True
        now = monotonic()
        if now - self.tick >= 1:
            with self.frame_lock:
                total = self.frames
            if total != self.frame_mark:
                self.last_frame = now
            if not self.copy_frames and total:
                self.ready = True
            if self.ready:
                if now - self.last_frame >= 5:
                    self.poll_id = 0
                    self.fail("The camera stopped sending video. Check the connection and start the preview again.")
                    return GLib.SOURCE_REMOVE
                self.on_rate((total - self.frame_mark) / (now - self.tick))
            elif now - self.started >= 10:
                self.poll_id = 0
                self.fail("No video arrived. Choose another capture mode or check the camera connection.")
                return GLib.SOURCE_REMOVE
            self.tick, self.frame_mark = now, total
        return GLib.SOURCE_CONTINUE

    def draw(self, sample):
        layout = GstVideo.VideoInfo.new_from_caps(sample.get_caps())
        buffer = sample.get_buffer()
        meta = GstVideo.buffer_get_video_meta(buffer)
        stride, offset = ((meta.stride[0], meta.offset[0]) if meta
                          else (layout.stride[0], layout.offset[0]))
        if stride < layout.width * 4 or offset < 0 or buffer.get_size() < offset + stride * layout.height:
            raise RuntimeError("The preview received an unsupported video buffer layout.")
        pixels = GLib.Bytes.new(buffer.extract_dup(offset, stride * layout.height))
        texture = Gdk.MemoryTexture.new(
            layout.width, layout.height, Gdk.MemoryFormat.R8G8B8A8, pixels, stride
        )
        self.picture.set_paintable(texture)

    def bus_message(self, _bus, message):
        if message.type == Gst.MessageType.ERROR:
            error, _debug = message.parse_error()
            self.fail(error.message)
        elif message.type == Gst.MessageType.EOS:
            self.fail("The camera stream ended.")

    def fail(self, message):
        self.stop()
        self.on_error(message)

    def stop(self):
        if self.poll_id:
            GLib.source_remove(self.poll_id)
            self.poll_id = 0
        if self.bus:
            self.bus.disconnect(self.bus_handler)
            self.bus.remove_signal_watch()
            self.bus = None
        if self.pipeline is not None:
            self.pipeline.set_state(Gst.State.NULL)
            self.pipeline = None
        self.picture.set_paintable(None)
        self.sink = None
