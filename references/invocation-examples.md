# Invocation examples

## Minimal autonomous production

```text
Use $produce-video-podcast on the attached audio and transcript. Preserve the audio, infer semantic chapters, choose the strongest public-safe visual treatment, and deliver a publish-ready MP4, samples, episode.json, contact sheet, reusable master, and QA report. Make reasonable creative decisions automatically and ask only when a required input cannot be inferred.
```

## Chinese single-speaker program

```text
使用 $produce-video-podcast 制作这期中文单人视频播客。音频和校正版字幕是唯一时间基准，不修改原音频。请自动划分语义段落与章节，制作真实比例进度轴、金句、证据卡、字幕和自然尾声；素材不得重复、循环或冻结。输出正式成片、章节样片、关键帧、接触表、母版工程和质检报告。
```

## Two-speaker program

```text
Use $produce-video-podcast to create a two-speaker video podcast from these files. Speaker A must stay in the top seat and Speaker B in the bottom seat. Use the transcript or diarization for real speaker intervals; show microphone and waves only for the active speaker and never invent overlapping speech. Render a handoff sample before the full video.
```

## Revision of an existing video

```text
Use $produce-video-podcast to audit and revise this existing video podcast. Check semantic timing, chapter progress, title wrapping, caption safety, evidence-card spacing, repeated footage, speaker activity, and the final two-second tail. Preserve approved content, repair the identified problems, and return a new version plus before/after QA evidence.
```

## Handoff to an AI without Codex Skills

```text
Follow the attached produce-video-podcast/SKILL.md as the governing workflow. Read its first-run checklist, episode schema, layout rules, and QA checklist. Use episode.json as the only timeline source. If HyperFrames is unavailable, implement the same contract in an equivalent deterministic renderer and document the substitution.
```
