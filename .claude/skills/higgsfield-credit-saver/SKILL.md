---
name: higgsfield-credit-saver
description: Credit-saving workflow for making AI video with Higgsfield. Plan in Claude, lock the look with one still, test cheap (Seedance 2.5 Flash, 720p, audio off), make one version, then batch. Every paid step gets a free cost estimate and a balance check first. Use whenever the user asks to make, test or batch videos or images on Higgsfield, or mentions saving credits.
---

# Higgsfield credit saver

Source: credit-saving tips from a creator reel (David Ho). The credit figures below are the reel's examples. Always check live prices with the free estimate tools, because prices change.

## Rule zero: estimate before every paid call

Before any `generate_image`, `generate_video` or `*_batch` call:
1. Call `balance` (free).
2. Call `estimate_image_cost` / `estimate_video_cost` (free) with the exact params you will send.
3. Tell the user the cost and their balance. If the balance can't cover the step, stop and say how many credits are needed. Never downgrade or switch models silently to make it fit.
4. Generate with the `quote_ref` from the estimate, so the request is exactly what was priced.
5. Pass `use_unlim: false` unless the user chose to spend unlimited generations.

## The four steps

### 1. Plan in Claude, then make one still to lock the look
- Write the plan first: subject, format (aspect ratio, clip length, number of clips), palette, style, camera, and one line per clip. Save it as a file (e.g. `video-plan.md`).
- Make ONE still image (default `gpt_image_2_6`, which costs about 0.75 credits) that shows the look.
- Show it to the user and wait for approval before animating. Changing the look on a still costs cents; changing it on a video costs a full clip.
- Reuse the approved still as the reference (`image_references` or `start_image`, mode `omni_reference`) on every clip, so the clips stay consistent.

### 2. Test with Seedance 2.5 Flash at 720p
- Model `seedance_2_5_flash`, `resolution: "720p"`. Reel figure: 25 credits vs 35 for the full model.
- Move to the full model or a higher resolution only for the final version, and only if the user asks.

### 3. Leave audio off while testing
- Set `generate_audio: false` (Seedance defaults to `true`). On Kling, sound costs extra (reel figure: 10 vs 7.5 credits).
- Add audio only on the final, approved version.

### 4. Make one version, check it, then batch
- Generate ONE clip, wait with `jobs_wait`, show it with `show_generation_by_ids`, and get the user's OK.
- Only then run the rest with `generate_video_batch`. Reel figure: 35 credits for one test vs 140 for four blind.
- Before the batch, estimate the whole batch (cost per clip × count) and confirm it against the balance.

## Checklist (run in order)
- [ ] Plan written and saved
- [ ] `balance` checked
- [ ] Still estimated → generated → user approved
- [ ] Test clip estimated (Flash, 720p, audio off) → generated → user approved
- [ ] Batch estimated (per clip × count) and confirmed against the balance → generated
- [ ] All results shown in one `show_generation_by_ids`
