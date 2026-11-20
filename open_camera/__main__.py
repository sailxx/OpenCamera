import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="Open Camera for Linux")
    parser.add_argument("--test-source", action="store_true", help="Show a GStreamer test camera")
    parser.add_argument("--smoke-test", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args()
    if sys.platform != "linux":
        parser.exit(1, "Open Camera requires Linux with GTK 4 and GStreamer. See README.md.\n")
    try:
        from .application import OpenCamera
    except (ImportError, ValueError) as error:
        parser.exit(1, f"Could not load GTK 4, libadwaita or GStreamer: {error}\nSee README.md.\n")
    return OpenCamera(args.test_source or args.smoke_test, smoke_test=args.smoke_test).run([sys.argv[0]])


if __name__ == "__main__":
    raise SystemExit(main())
