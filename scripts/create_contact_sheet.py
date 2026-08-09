from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a timed video contact sheet with FFmpeg")
    parser.add_argument("video", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--times", required=True, help="Comma-separated seconds")
    parser.add_argument("--columns", type=int, default=4)
    parser.add_argument("--width", type=int, default=480)
    args = parser.parse_args()
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        raise SystemExit("FFmpeg was not found on PATH")
    times = [float(value.strip()) for value in args.times.split(",") if value.strip()]
    if not times:
        raise SystemExit("At least one timestamp is required")
    rows = (len(times) + args.columns - 1) // args.columns
    selects = "+".join(f"between(t\\,{value:.3f}\\,{value + 0.040:.3f})" for value in times)
    vf = f"select='{selects}',scale={args.width}:-2,tile={args.columns}x{rows}"
    command = [ffmpeg, "-hide_banner", "-loglevel", "error", "-i", str(args.video),
               "-vf", vf, "-frames:v", "1", "-q:v", "2", "-y", str(args.output)]
    subprocess.run(command, check=True)
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
