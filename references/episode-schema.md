# Episode data interface

Use one UTF-8 `episode.json` as the authoritative timeline.

## Program fields

| Field | Type | Meaning |
|---|---|---|
| `title` | string | Program title |
| `duration` | number | Total seconds, including tail |
| `content_end` | number | Time when progress reaches 100% |
| `audio` | string | Local audio path relative to the project |
| `captions` | string | Timed SRT or equivalent path |
| `layout_mode` | string | `single`, `dual_stacked`, or `multi` |
| `brand` | object | Optional name, byline, colors, and logo |
| `outro` | object | Optional author, follow prompt, next episode, and tail duration |
| `chapters` | array | Ordered chapter intervals |
| `segments` | array | Continuous semantic intervals |
| `speakers` | array | Speaker identities and fixed seats |
| `speaker_intervals` | array | Real activity intervals |

Require `0 < content_end <= duration`. Require continuous segments from zero through `content_end`.

## Chapter

```json
{
  "id": "chapter-1",
  "number": "01",
  "title": "Opening question",
  "start": 0.0,
  "end": 30.22
}
```

Derive chapter count from `chapters.length`; never hardcode `/05`.

## Segment

```json
{
  "index": 1,
  "start": 0.0,
  "end": 8.18,
  "chapter_id": "chapter-1",
  "label": "Opening",
  "title": "Why do we project emotion onto distant heroes?",
  "title_lines": ["Why do we project emotion", "onto distant heroes?"],
  "keyword": "Emotional projection",
  "body": "A short context sentence.",
  "quote": "A readable sentence that remains faithful to the narration.",
  "visual_mode": "evidence",
  "visual_items": []
}
```

Use `title_lines` only when it improves semantic wrapping. A renderer should prefer it over automatic wrapping.

## Speaker

```json
{
  "id": "speaker_a",
  "display_name": "Speaker A",
  "avatar": "assets/speaker-a.png",
  "accent": "#EE911B",
  "seat": "bottom"
}
```

In `dual_stacked`, reserve `top` and `bottom`. Do not swap these values when activity changes.

## Speaker interval

```json
{"speaker_id": "speaker_a", "start": 0.0, "end": 5.3}
```

Overlaps are allowed only when the source contains real overlapping speech.

## Evidence window

Attach this object to a segment:

```json
{
  "asset": "assets/context-01.mp4",
  "start": 2.0,
  "source_start": 11.5,
  "duration": 7.0,
  "grade": "B",
  "label": "Context footage",
  "boundary_note": "Provides context; does not prove population attitudes.",
  "source": "Optional provenance note"
}
```

Keep the authored window inside its segment and source duration. Do not repeat an asset unless the user explicitly authorizes reuse for a meaningful reason.

An evidence grade tag may reduce in size or emphasis after about two seconds, but its footer label and boundary note must remain readable.
