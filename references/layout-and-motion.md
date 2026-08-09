# Layout and motion rules

## 16:9 default zones

- Canvas: 1920×1080.
- Top progress area: y=38–120.
- Main content: y=150–830.
- Speaker column: x=40–285.
- Captions: begin at x=320; bottom margin about 52px.
- Evidence card: default 900×630, with a 16:9 900×506 media region and 124px footer.
- Evidence-to-caption gap: 80–110px.

Scale proportionally for other aspect ratios while retaining disjoint zones.

## Typography

- Use readable CJK-capable fonts when Chinese is present.
- Treat scene titles as the primary hierarchy and context copy as secondary.
- Keep current chapter name at 24–26px or the proportional equivalent.
- Avoid isolated single-character title lines. Prefer explicit `title_lines`.
- Allow sufficient quote display time; do not animate every word continuously.

## Progress and chapters

- Animate fill and playhead linearly from zero to `content_end`.
- Compute node x-position as `left + chapter.start / content_end * usable_width`.
- Render only node numbers on the rail.
- Activate the current node with color and about 8% scale; restore older nodes to neutral.
- Hold the full rail throughout the tail.

## Speakers

- `single`: render only the active program speaker.
- `dual_stacked`: keep top and bottom identities fixed.
- Active: full brightness, accent border, microphone, and restrained wave animation.
- Inactive: about 58% opacity/brightness, name retained, no microphone or wave.
- Reserve 22–28px between dual avatars; use roughly 168–176px avatars on 1080p.

## Evidence and return state

- Show evidence for 6–9 seconds or less than the remaining real source duration.
- Use `object-fit: contain` or a justified `cover`; do not distort aspect ratio.
- Keep grade, label, and boundary note visible in the footer.
- After evidence ends, return to a quote, diagram, speaker stage, or structured graphic.
- Do not leave empty media boxes.

## Transitions and tail

- Align scene visibility exactly to semantic boundaries.
- Pre-roll internal entrance animation while the next timed scene is hidden, so the cut never produces an empty half-second.
- Use transforms and opacity for motion; avoid layout-property animation.
- Keep the final conclusion visible for a 1.5–2.5 second tail and reduce its intensity gradually.
