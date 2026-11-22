#!/bin/bash
set -euo pipefail

export DISPLAY=:99 GTK_A11Y=none GSK_RENDERER=cairo
Xvfb "$DISPLAY" -screen 0 1280x800x24 -nolisten tcp &
xvfb_pid=$!
app_pid=
cleanup() {
    if [[ -n "$app_pid" ]]; then kill "$app_pid" 2>/dev/null || true; fi
    kill "$xvfb_pid" 2>/dev/null || true
}
trap cleanup EXIT

for attempt in {1..50}; do
    if [[ -S /tmp/.X11-unix/X99 ]]; then
        timeout --kill-after=5s 55s "$@" --smoke-test
        if [[ -n "${OPEN_CAMERA_PREVIEWS:-}" ]]; then
            for scheme in dark light; do
                ADW_DEBUG_COLOR_SCHEME="prefer-$scheme" "$@" --test-source &
                app_pid=$!
                window=$(timeout 10s xdotool search --sync --onlyvisible --pid "$app_pid" --name '^Open Camera$' | head -n 1)
                sleep 1
                import -window "$window" "$OPEN_CAMERA_PREVIEWS/workbench-$scheme.png"
                kill "$app_pid"
                wait "$app_pid" || true
                app_pid=
            done
        fi
        exit
    fi
    kill -0 "$xvfb_pid"
    sleep .1
done

echo "Xvfb did not become ready." >&2
exit 1
