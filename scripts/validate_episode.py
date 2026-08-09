from __future__ import annotations

import argparse
import json
from pathlib import Path


def validate(data: dict) -> list[str]:
    errors: list[str] = []
    duration = float(data.get("duration", 0))
    content_end = float(data.get("content_end", 0))
    if not 0 < content_end <= duration:
        errors.append("content_end must be greater than zero and no greater than duration")

    segments = data.get("segments", [])
    if not segments:
        errors.append("segments must not be empty")
    cursor = 0.0
    assets: set[str] = set()
    chapter_ids = {item.get("id") for item in data.get("chapters", [])}
    for position, segment in enumerate(segments, 1):
        start = float(segment.get("start", -1))
        end = float(segment.get("end", -1))
        if abs(start - cursor) > 0.001:
            errors.append(f"segment {position} starts at {start}, expected {cursor}")
        if end <= start:
            errors.append(f"segment {position} has invalid duration")
        if segment.get("chapter_id") not in chapter_ids:
            errors.append(f"segment {position} references an unknown chapter")
        lines = segment.get("title_lines")
        if lines is not None and (not isinstance(lines, list) or not all(isinstance(line, str) and line.strip() for line in lines)):
            errors.append(f"segment {position} title_lines must be a list of non-empty strings")
        evidence = segment.get("evidence_window")
        if evidence:
            ev_start = float(evidence.get("start", -1))
            ev_duration = float(evidence.get("duration", 0))
            if ev_duration <= 0 or ev_duration > 9:
                errors.append(f"segment {position} evidence duration must be in (0, 9]")
            if ev_start < start or ev_start + ev_duration > end + 0.001:
                errors.append(f"segment {position} evidence escapes its segment")
            asset = evidence.get("asset")
            if asset in assets:
                errors.append(f"evidence asset is reused: {asset}")
            if asset:
                assets.add(asset)
            for field in ("grade", "label", "boundary_note"):
                if not evidence.get(field):
                    errors.append(f"segment {position} evidence is missing {field}")
        cursor = end
    if segments and abs(cursor - content_end) > 0.001:
        errors.append(f"segments end at {cursor}, expected content_end {content_end}")

    chapters = data.get("chapters", [])
    for position, chapter in enumerate(chapters, 1):
        start = float(chapter.get("start", -1))
        end = float(chapter.get("end", -1))
        if end <= start:
            errors.append(f"chapter {position} has invalid duration")
        if position > 1 and abs(start - float(chapters[position - 2].get("end", -2))) > 0.001:
            errors.append(f"chapter {position} is not continuous")

    speaker_ids = {item.get("id") for item in data.get("speakers", [])}
    for interval in data.get("speaker_intervals", []):
        if interval.get("speaker_id") not in speaker_ids:
            errors.append("speaker interval references an unknown speaker")
        if float(interval.get("end", 0)) <= float(interval.get("start", 0)):
            errors.append("speaker interval has invalid duration")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a public video-podcast episode.json")
    parser.add_argument("episode", type=Path)
    args = parser.parse_args()
    data = json.loads(args.episode.read_text(encoding="utf-8"))
    errors = validate(data)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("OK: episode timeline and data interface are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
