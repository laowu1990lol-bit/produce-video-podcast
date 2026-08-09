# QA and release checklist

## Timeline

- Validate every segment at boundary minus 0.1s and plus 0.1s.
- Validate every chapter at its exact start and shortly after activation.
- Measure rail/playhead position at 25%, 50%, 75%, and 100%; require error no greater than 1%.
- Confirm 100% is held during the tail.

## Media

- Probe every file before authoring.
- Ensure evidence duration does not exceed the real source duration.
- Reject unintended duplicate asset hashes and perceptual duplicates.
- Reject `loop`, reverse, mirror-as-disguise, or frozen final frames.
- Check aspect ratio, black frames, decoding gaps, and unintended stillness.

## Layout

- Run renderer lint, runtime, layout, motion, and contrast checks.
- Require zero errors and zero warnings for the release composition.
- Confirm captions do not enter the speaker column.
- Confirm evidence-to-caption spacing is 80–110px at 1080p.
- Check long titles and CJK line breaks manually.

## Speaker behavior

- Validate single mode with all unused speakers absent.
- Validate fixed seat order in multi-speaker modes.
- Check active/inactive microphone, wave, border, and brightness states.
- Confirm overlapping activity matches real overlapping audio.

## Audio and packaging

- Preserve the original speech unless the user authorizes edits.
- Default spoken-word target: approximately -16 LUFS, true peak no higher than -1.5 dBTP.
- Deliver H.264/AAC MP4 unless the platform requires another format.
- Include a contact sheet, boundary frames, reusable project, and concise QA report.
- State source or licensing limitations. Never call contextual footage factual proof.
