from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def duration(path: Path, ffprobe: str) -> float:
    command = [ffprobe, "-v", "error", "-show_entries", "format=duration", "-of", "json", str(path)]
    data = json.loads(subprocess.check_output(command, text=True, encoding="utf-8"))
    return float(data["format"]["duration"])


def frame_hash(path: Path, second: float, ffmpeg: str, mirror: bool = False) -> int:
    filters = "scale=32:32,format=gray"
    if mirror:
        filters = "hflip," + filters
    command = [ffmpeg, "-hide_banner", "-loglevel", "error", "-ss", f"{second:.3f}", "-i", str(path),
               "-frames:v", "1", "-vf", filters, "-f", "rawvideo", "-"]
    pixels = subprocess.check_output(command)
    if len(pixels) != 1024:
        raise RuntimeError(f"could not extract a 32x32 frame from {path}")
    average = sum(pixels) / len(pixels)
    value = 0
    for pixel in pixels:
        value = (value << 1) | int(pixel >= average)
    return value


def similarity(left: int, right: int) -> float:
    return 1.0 - (left ^ right).bit_count() / 1024.0


def fingerprints(path: Path, ffmpeg: str, ffprobe: str) -> tuple[list[int], list[int]]:
    length = duration(path, ffprobe)
    points = [max(0.0, length * fraction) for fraction in (0.25, 0.5, 0.75)]
    normal = [frame_hash(path, point, ffmpeg) for point in points]
    mirrored = [frame_hash(path, point, ffmpeg, mirror=True) for point in points]
    return normal, mirrored


def main() -> int:
    parser = argparse.ArgumentParser(description="Detect exact and visually suspicious video reuse")
    parser.add_argument("videos", nargs="+", type=Path)
    parser.add_argument("--threshold", type=float, default=0.88)
    args = parser.parse_args()
    ffmpeg, ffprobe = shutil.which("ffmpeg"), shutil.which("ffprobe")
    if not ffmpeg or not ffprobe:
        raise SystemExit("FFmpeg and FFprobe must be available on PATH")
    for path in args.videos:
        if not path.is_file():
            raise SystemExit(f"missing file: {path}")
    hashes = {path: sha256(path) for path in args.videos}
    prints = {path: fingerprints(path, ffmpeg, ffprobe) for path in args.videos}
    findings = 0
    for index, left in enumerate(args.videos):
        for right in args.videos[index + 1:]:
            if hashes[left] == hashes[right]:
                print(f"EXACT\t{left}\t{right}")
                findings += 1
                continue
            left_normal, _ = prints[left]
            right_normal, right_mirrored = prints[right]
            direct = sum(similarity(a, b) for a, b in zip(left_normal, right_normal)) / 3
            mirror = sum(similarity(a, b) for a, b in zip(left_normal, right_mirrored)) / 3
            score = max(direct, mirror)
            if score >= args.threshold:
                mode = "mirrored" if mirror > direct else "direct"
                print(f"SUSPECT\t{score:.3f}\t{mode}\t{left}\t{right}")
                findings += 1
    print(f"Checked {len(args.videos)} files; findings: {findings}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
