# First-time setup and episode intake

Use this checklist before building the first project. Distinguish one-time environment setup from material required for each episode.

## One-time environment setup

Confirm or install:

- a renderer capable of deterministic HTML/video timing, preferably HyperFrames when available;
- FFmpeg and FFprobe on `PATH` or at a known local path;
- Python 3.10+ for validation and QA scripts;
- a Chromium-compatible browser when the renderer requires it;
- fonts that cover the program language, especially CJK text;
- a writable project directory with separate `work/` and final-output locations;
- enough disk space for extracted frames and at least two full renders.

Run a short sample before rendering a program longer than one minute.

## Minimum required for each episode

The user must provide or explicitly authorize creation of:

1. **Primary audio or video** — the narration, interview, or podcast recording.
2. **Timed words** — an SRT/ASS/timed JSON transcript, or permission to transcribe the recording.
3. **Publishing target** — platform or at least aspect ratio; default to 1920×1080 landscape when unspecified.
4. **Speaker mapping** — speaker names or stable IDs and, for multiple speakers, who speaks in each interval. Diarization may supply a draft but must not invent identities.
5. **Output language** — caption and on-screen-text language.
6. **Rights boundary** — confirmation that supplied audio, portraits, logos, and footage may be used for the intended release, or an instruction to use public/synthetic placeholders only.

If one of these is missing and cannot be safely inferred from the files, ask for it before the full render.

## Strongly recommended inputs

- corrected transcript or pronunciation list;
- desired duration and whether the full audio must remain unchanged;
- program name, author/byline, logo, accent color, and font preference;
- speaker portraits with display names and preferred fixed seats;
- existing intro/outro, music, or sonic identity;
- approved supporting footage with provenance notes;
- reference videos or screenshots showing desired density and style;
- preferred number of semantic scenes, quotes, and chapters;
- platform-safe title, description, and cover requirements;
- explicit permission for the agent to choose defaults without repeated approval.

The workflow must still work when these are absent. Use neutral branding, text-led graphics, and clearly labeled contextual footage.

## Material-preparation rules

- Preserve original files; copy or reference them from the project.
- Prefer WAV or high-quality lossless audio for the master.
- Prefer UTF-8 SRT with millisecond timing.
- Use square portraits at least 512×512px; transparent PNG is preferred but not required.
- Record the real duration, frame rate, dimensions, audio sample rate, and channel count of every media file.
- Keep a source-and-rights note for every external video or image.

## Copyable episode handoff template

```text
Use $produce-video-podcast to create a publish-ready video podcast.

Primary audio/video:
Transcript or subtitles:
Permission to transcribe if needed: yes / no
Output language:
Publishing platform and aspect ratio:
Program title:
Author/byline:
Speakers and portrait files:
Single or multi-speaker layout:
Logo, colors, and visual references:
Approved supporting footage:
Footage rights/provenance notes:
Keep the original audio unchanged: yes / no
Desired chapters, quotes, or duration:
May the agent choose unspecified creative details: yes / no
Output folder:

Required deliverables:
- final MP4
- captions
- semantic timeline and episode.json
- chapter-boundary sample
- speaker-handoff sample when applicable
- contact sheet and keyframes
- reusable master project
- QA report
```

## Minimum one-line invocation

When the files are already attached, this is sufficient:

```text
Use $produce-video-podcast on the attached audio and transcript. Preserve the audio, infer semantic chapters, choose the best public-safe visuals, and deliver the final video, samples, timeline, contact sheet, reusable project, and QA report. Ask only if a required input cannot be inferred.
```
