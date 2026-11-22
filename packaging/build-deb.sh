#!/bin/bash
set -euo pipefail

version=${1:?release version required}
mkdir -p dist
stage=$(mktemp -d)
trap 'rm -rf -- "$stage"' EXIT
bash packaging/stage.sh "$stage"
install -d "$stage/DEBIAN"
cat > "$stage/DEBIAN/control" <<EOF
Package: open-camera
Version: $version
Section: video
Priority: optional
Architecture: all
Maintainer: sailxx <172365404+sailxx@users.noreply.github.com>
Depends: python3 (>= 3.10), python3-gi, gir1.2-gtk-4.0 (>= 4.8), gir1.2-adw-1 (>= 1.4), gir1.2-gstreamer-1.0 (>= 1.20), gir1.2-gst-plugins-base-1.0 (>= 1.20), gstreamer1.0-plugins-base, gstreamer1.0-plugins-good, librsvg2-common, v4l-utils
Description: Native Linux camera workbench
 Preview a Video4Linux camera, inspect capture modes and adjust
 controls exposed by the camera driver.
EOF
dpkg-deb --root-owner-group --build "$stage" "dist/open-camera_${version}_all.deb"
