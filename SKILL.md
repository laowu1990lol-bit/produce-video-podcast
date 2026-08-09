---
name: produce-video-podcast
description: Produce, revise, validate, and package publish-ready video podcasts from local audio or video, transcripts, subtitles, speaker portraits, and supporting footage. Use when Codex must create a single-speaker or multi-speaker video podcast; build semantic scenes and real-time chapter progress; synchronize captions, quotes, evidence cards, speaker activity, microphones, and wave effects; prevent repeated or looping footage; repair broken timelines or layout gaps; render samples and a final MP4; or deliver contact sheets, boundary frames, QA reports, and a reusable master project.
---

# Produce Video Podcast

Create the program around one authoritative `episode.json`. Treat audio and corrected captions as the timing baseline; do not maintain competing scene, chapter, speaker, or media timelines.

## Run the first-time intake

Read [first-run-checklist.md](references/first-run-checklist.md) before doing any project work. Inventory the supplied items against its required and optional lists. Report missing required inputs in one concise message. Do not request optional items when a safe default or generated placeholder will preserve the user's intent.

## Start from the supplied material

1. Inspect every supplied audio, transcript, subtitle, portrait, logo, video, and workflow file.
2. Determine the program duration, language, aspect ratio, speaker count, publishing context, and whether the transcript already contains reliable timestamps.
3. Transcribe only when reliable timed text is absent. Preserve supplied wording unless the user authorizes editorial rewriting.
4. Ask only for choices that materially change the result. When the user delegates creative control, select defensible defaults and continue.

## Build the content model

Read [episode-schema.md](references/episode-schema.md) before creating or modifying `episode.json`.

1. Segment by semantic change, not equal duration. Use corrected caption boundaries as exact cut points.
2. Write concise scene titles, context text, and quotes that remain faithful to the narration.
3. Add `title_lines` when automatic wrapping would create isolated one-character or one-word lines.
4. Place chapter nodes at their actual time ratios. Derive the displayed chapter count from the data.
5. Define speaker intervals from real speech. Never invent simultaneous activity.
6. Give every evidence window a grade, label, boundary note, source start, and finite duration.

Run:

```powershell
python scripts/validate_episode.py path/to/episode.json
```

Fix every reported error before authoring the composition.

## Author the composition

Read [layout-and-motion.md](references/layout-and-motion.md). Prefer HyperFrames HTML when available because it supports deterministic timing, inspection, and rendering. A different renderer is acceptable only if it preserves the same data interface and QA requirements.

Implement these invariants:

- Start progress at 0%; reach 100% at `content_end`; hold full during the tail.
- Keep evidence video at its natural aspect ratio and attach a persistent explanatory footer.
- Stop footage after 6–9 seconds or before its real end. Do not loop, freeze, mirror, reverse, or cosmetically transform footage to disguise reuse.
- Replace ended footage with a graphic, quote, diagram, or speaker stage.
- Keep caption and speaker columns disjoint.
- In `dual_stacked`, keep seat identity fixed. Change activity state, never seat order.
- Keep the final scene visible during the tail and fade its content gradually.

## Validate before the full render

Read [qa-and-release.md](references/qa-and-release.md).

1. Run syntax, runtime, layout, motion, and contrast checks.
2. Render a chapter-boundary sample.
3. For multiple speakers, render a handoff sample.
4. Inspect keyframes at every semantic boundary and immediately before and after each chapter boundary.
5. Confirm progress at 25%, 50%, 75%, and 100% with no more than 1% error.
6. Run `python scripts/detect_media_reuse.py <video files...>` and inspect every suspicious pair.
7. Render the final only after samples pass.
8. Normalize spoken-word audio near -16 LUFS unless the target platform specifies otherwise.

## Deliver

Provide:

- publish-ready MP4;
- semantic-boundary contact sheet;
- chapter-boundary keyframes;
- speaker-layout sample when applicable;
- boundary sample;
- `episode.json` and reusable master project;
- QA report that states remaining limits rather than claiming absolute correctness.

Use `scripts/create_contact_sheet.py` to generate a timed contact sheet when FFmpeg is available.

When the user asks how to invoke or hand off the workflow, provide an appropriate prompt from [invocation-examples.md](references/invocation-examples.md) and adapt its file fields to the actual attachments.

## Public-skill constraints

- Do not bundle user audio, news footage, private portraits, credentials, licensed fonts, or copyrighted media.
- Keep brand names, colors, portraits, logos, bylines, and column titles configurable.
- Include only synthetic placeholders or user-authorized public assets in redistributed packages.
- Preserve provenance and evidence-boundary notes in project data.
