#!/bin/bash
set -euo pipefail

version=${1:?release version required}
out=$PWD/dist
mkdir -p "$out"
top=$(mktemp -d)
trap 'rm -rf -- "$top"' EXIT
package="open-camera-$version"
mkdir -p "$top/SOURCES" "$top/$package"
cp -r open_camera packaging design "$top/$package/"
tar -C "$top" -czf "$top/SOURCES/$package.tar.gz" "$package"
rpmbuild -bb --define "_topdir $top" --define "app_version $version" packaging/open-camera.spec
cp "$top"/RPMS/noarch/*.rpm "$out/"
