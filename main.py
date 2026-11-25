# news-image-20261125 v1 — "The World in One Day", Wednesday 25 November 2026.
#
# A newspaper front page summing up the world's news of Wednesday 25
# November 2026 in one image: 35 verified stories across 9 regions and
# 16 fields, with a giant date masthead, a six-number stats strip, a
# colour-coded region bar, a UTC timeline, 3 illustrated heroes with
# status tags, a numbered ILLUSTRATED grid (stories 4-19, each with its
# own AI-generated photo thumbnail), a 16-story ALSO list, a dot-matrix
# world map marking the 9 regions, a DATE CHECK naming the prior-day
# stories deliberately left out, and a HOW WE CHECKED footer.
#
# Dense text is typeset HTML, never drawn by an image model; the three
# hero illustrations and the 16 grid thumbnails are AI-generated
# photographs (no text in any of them). The world map is a hand-drawn
# SVG dot matrix.
#
# Python 3.13, standard library only. The entry image sits beside this
# file as entry.png (1024x1024 PNG, under 1 MiB). The program validates
# it — PNG signature, IHDR dimensions, byte size, SHA-256 — then copies
# it byte-for-byte to $MAKEFUN_OUTPUT_DIR (or /output). It reads nothing
# else, makes no network calls, and holds no secrets, so repeated runs
# are byte-identical.

import hashlib
import os
import sys

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
HERE = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(HERE, "entry.png")

# SHA-256 of the final v1 entry.png (1024x1024, 599,085 bytes).
# Filled in after the final render; update it whenever entry.png changes.
EXPECTED_SHA256 = "4fc80934a7cddf5091ad786ed0493488ebfaaea1fc555169d6251ed5e311d028"
EXPECTED_BYTES = 599085
ONE_MIB = 1_048_576


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def main():
    with open(IMAGE_PATH, "rb") as handle:
        data = handle.read()

    if data[1:4] != b"PNG":
        fail("entry.png is not a PNG file")
    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    if (width, height) != (1024, 1024):
        fail(f"entry.png is {width}x{height}, expected 1024x1024")
    if len(data) > ONE_MIB:
        fail(f"entry.png is {len(data)} bytes, over the 1 MiB limit")
    if len(data) != EXPECTED_BYTES:
        fail(f"entry.png is {len(data)} bytes, expected {EXPECTED_BYTES}")
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        fail(f"entry.png sha256 mismatch: got {digest}")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(OUTPUT_DIR, "entry.png")
    with open(out_path, "wb") as handle:
        handle.write(data)
    # Read the copy back and confirm it is the same validated image, so a
    # partial or failed write can never pass silently as a success.
    with open(out_path, "rb") as handle:
        written = handle.read()
    if hashlib.sha256(written).hexdigest() != EXPECTED_SHA256:
        fail("written entry.png sha256 mismatch")
    print(f"entry.png verified ({len(data)} bytes, sha256 {digest[:12]}...)")


if __name__ == "__main__":
    main()
