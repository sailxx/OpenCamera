#!/bin/sh
set -eu

root=${1:?staging directory required}
install -d "$root/usr/share/open-camera/open_camera"
install -m 0644 open_camera/*.py "$root/usr/share/open-camera/open_camera/"
install -m 0644 open_camera/workbench.css open_camera/workbench-scene.jpg "$root/usr/share/open-camera/open_camera/"
install -d "$root/usr/share/open-camera/open_camera/icons"
install -m 0644 open_camera/icons/*.svg "$root/usr/share/open-camera/open_camera/icons/"
install -Dm755 packaging/open-camera "$root/usr/bin/open-camera"
install -Dm644 packaging/io.github.sailxx.OpenCamera.desktop "$root/usr/share/applications/io.github.sailxx.OpenCamera.desktop"
install -Dm644 design/open-camera.svg "$root/usr/share/icons/hicolor/scalable/apps/io.github.sailxx.OpenCamera.svg"
