---
name: testing-explosive-games
description: Test the Explosive Games S2 Flask app end-to-end. Use when verifying template rendering, shared asset loading, overlay interactions, or route progression.
---

## Local Dev Setup

1. Install dependencies: `pip install flask`
2. Start the server: `python app.py` (runs on port 5000 by default)
3. If port 5000 is occupied, run on an alternate port:
   ```python
   python -c "from app import app; app.run(host='0.0.0.0', port=5001)"
   ```
4. Verify: `curl -s -o /dev/null -w '%{http_code}' http://localhost:5001/level1` should return `200`

## Route Structure

| Route | Level | Template |
|-------|-------|----------|
| `/` | Redirect | -> `/level1` |
| `/level1` | Level 1 | `level1.html` |
| `/level2_69` | Level 2 | `level2.html` |
| `/level3_nig` | Level 3 | `level3.html` |
| `/level4` | Final | Inline HTML |

All levels use GET to render and POST to advance to the next level.

## Key Testing Patterns

### Verify shared assets load correctly
Check page source for shared CSS/JS imports from base template:
```bash
curl -s http://localhost:5001/level1 | grep -E '(shared\.css|overlay\.js|class="overlay")'
```
Expect: `shared.css` link, `overlay.js` script, `class="overlay"` on overlay divs.

### Verify .hidden class
Level 2 uses `class="hidden"` from `shared.css` to hide elements initially. If shared CSS fails to load, hidden elements will be visible on page load.

### Verify overlay JS functions
Level 1 and Level 3 call `showOverlay()` / `hideOverlay()` from `overlay.js`. If the script fails to load, clicking doors or dragging the plane will produce JS errors ("showOverlay is not defined").

### Verify route handler factory
Test POST progression via curl:
```bash
curl -s -o /dev/null -w '%{http_code} %{redirect_url}' -X POST http://localhost:5001/level1
# Expect: 302 http://localhost:5001/level2_69
```

## Level-Specific Interactions

- **Level 1**: Drag-and-drop plane onto tower images. Triggers overlay on drop.
- **Level 2**: Text input riddles. Type answer and click SUBMIT. Correct answer shows image overlay.
- **Level 3**: Click doors 1-5. Doors 1-4 show wrong images via overlay. Door 5 plays a video.

## No CI Configured

This repo has no CI checks. Testing is manual via browser.

## Devin Secrets Needed

None - no authentication or external services required.
