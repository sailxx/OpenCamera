#!/bin/bash
set -euo pipefail

export DISPLAY=:99 GTK_A11Y=none GSK_RENDERER=cairo
Xvfb "$DISPLAY" -screen 0 1280x800x24 -nolisten tcp &
xvfb_pid=$!
trap 'kill "$xvfb_pid" 2>/dev/null || true' EXIT

for attempt in {1..50}; do
    if [[ -S /tmp/.X11-unix/X99 ]]; then
        timeout --kill-after=5s 55s "$@" --smoke-test
        exit
    fi
    kill -0 "$xvfb_pid"
    sleep .1
done

echo "Xvfb did not become ready." >&2
exit 1
