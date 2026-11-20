#!/bin/bash
set -euo pipefail

version=${1:?release version required}
out=$PWD/dist
mkdir -p "$out"
work=$(mktemp -d)
trap 'rm -rf -- "$work"' EXIT
appdir="$work/OpenCamera.AppDir"
bash packaging/stage.sh "$appdir"

# The build runs in a clean Ubuntu 24.04 x86_64 container. The host supplies glibc and graphics drivers.
install -d "$appdir/usr/lib" "$appdir/usr/share"
library_dir=/usr/lib/x86_64-linux-gnu
tar -C /usr/lib --exclude='*/dri' --exclude='*/ld-linux*' \
  --exclude='*/libc.so*' --exclude='*/libm.so*' --exclude='*/libmvec.so*' \
  --exclude='*/libpthread.so*' --exclude='*/libdl.so*' --exclude='*/librt.so*' \
  --exclude='*/libresolv.so*' --exclude='*/libutil.so*' --exclude='*/libthread_db.so*' \
  --exclude='*/libnss_*.so*' --exclude='*/libGL*.so*' --exclude='*/libEGL*.so*' \
  --exclude='*/libvulkan*.so*' --exclude='*/libgbm*.so*' --exclude='*/libdrm*.so*' \
  -cf - x86_64-linux-gnu | tar -C "$appdir/usr/lib" -xf -
cp -a /usr/lib/python3 /usr/lib/python3.12 "$appdir/usr/lib/"
python_binary=$(readlink -f /usr/bin/python3)
install -Dm755 "$python_binary" "$appdir/usr/bin/python3"
install -Dm755 /usr/bin/v4l2-ctl "$appdir/usr/bin/v4l2-ctl"
for folder in fonts glib-2.0 icons gtk-4.0 mime; do
  if [[ -d "/usr/share/$folder" ]]; then cp -a "/usr/share/$folder" "$appdir/usr/share/"; fi
done
install -Dm644 packaging/appimage-fonts.conf "$appdir/etc/fonts/fonts.conf"
glib-compile-schemas "$appdir/usr/share/glib-2.0/schemas"
loaders="$library_dir/gdk-pixbuf-2.0/2.10.0"
if [[ -s "$loaders/loaders.cache" ]]; then
  install -Dm644 "$loaders/loaders.cache" "$appdir$loaders/loaders.cache"
fi
install -m755 packaging/AppRun "$appdir/AppRun"
install -m644 packaging/io.github.sailxx.OpenCamera.desktop "$appdir/"
install -m644 design/open-camera.svg "$appdir/io.github.sailxx.OpenCamera.svg"
ln -s io.github.sailxx.OpenCamera.svg "$appdir/.DirIcon"

curl -fL --retry 3 -o "$work/appimagetool" \
  https://github.com/AppImage/appimagetool/releases/download/1.9.1/appimagetool-x86_64.AppImage
chmod +x "$work/appimagetool"
ARCH=x86_64 VERSION="$version" APPIMAGE_EXTRACT_AND_RUN=1 "$work/appimagetool" \
  "$appdir" "$out/OpenCamera-${version}-x86_64.AppImage"
chmod +x "$out/OpenCamera-${version}-x86_64.AppImage"
