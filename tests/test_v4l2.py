from fractions import Fraction
from unittest import TestCase
from unittest.mock import patch

from open_camera.v4l2 import Control, Device, inspect_device, parse_controls, parse_modes, write_control


class V4L2Tests(TestCase):
    def test_discrete_modes_keep_high_rates_and_format_specific_limits(self):
        output = """
    [0]: 'MJPG' (Motion-JPEG, compressed)
        Size: Discrete 1920x1080
            Interval: Discrete 0.008s (120.000 fps)
            Interval: Discrete 0.017s (59.940 fps)
        Size: Stepwise 120x90 - 800x600 with step 8/8
            Interval: Discrete 0.033s (30.000 fps)
    [1]: 'YUYV' (YUYV 4:2:2)
        Size: Discrete 640x480
            Interval: Discrete 0.017s (60.000 fps)
    [2]: 'UNKN'
        Size: Discrete 640x480
            Interval: Discrete 0.017s (60.000 fps)
"""
        modes = parse_modes(output)
        self.assertEqual([mode.fps for mode in modes],
                         [Fraction(120), Fraction(60000, 1001), Fraction(60)])
        self.assertEqual(modes[2].caps, "video/x-raw,format=YUY2,width=640,height=480,framerate=60/1")

    def test_driver_flags_and_menu_indices(self):
        output = """
      brightness 0x00980900 (int) : min=-64 max=64 step=2 default=0 value=-4
white_balance_auto 0x0098090c (bool) : default=1 value=1
       exposure 0x009a0902 (int) : min=1 max=5000 step=1 default=200 value=180 flags=inactive, volatile
  auto_exposure 0x009a0901 (menu) : min=0 max=3 default=3 value=3
                1: Manual Mode
                3: Aperture Priority Mode
"""
        brightness, automatic, exposure, menu = parse_controls(output)
        self.assertEqual((brightness.minimum, brightness.step, brightness.value), (-64, 2, -4))
        self.assertEqual([control.default for control in (brightness, automatic, exposure, menu)],
                         [0, 1, 200, 3])
        self.assertEqual(automatic.value, 1)
        self.assertFalse(exposure.writable)
        self.assertEqual(menu.choices, {1: "Manual Mode", 3: "Aperture Priority Mode"})

    @patch("open_camera.v4l2.invoke")
    def test_inspection_reports_partial_failure(self, invoke):
        invoke.side_effect = [RuntimeError("Permission denied"), " brightness 0x00980900 (int) : value=0"]
        modes, controls, errors = inspect_device(Device("/dev/video0", "Webcam"))
        self.assertEqual(modes, [])
        self.assertEqual(errors, ["Permission denied"])
        self.assertEqual(controls[0].name, "brightness")
        self.assertIsNone(controls[0].default)

    @patch("open_camera.v4l2.invoke")
    def test_write_rejects_invalid_value_before_touching_hardware(self, invoke):
        webcam = Device("/dev/video0", "Webcam")
        brightness = Control("brightness", "int", 0, 0, 10, 2)
        with self.assertRaises(ValueError):
            write_control(webcam, brightness, 3)
        invoke.assert_not_called()
        write_control(webcam, brightness, 4)
        invoke.assert_called_once_with("/dev/video0", "--set-ctrl", "brightness=4")
