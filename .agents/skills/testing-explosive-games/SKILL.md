---
name: testing-explosive-games-s2
description: Test the Explosive Games S2 Flask app end-to-end. Use when verifying game level UI, error handling, or route changes.
---

# Testing Explosive Games S2

## Setup

```bash
pip install flask
cd /path/to/Explosive-games-S2
python app.py
# Server runs on http://localhost:5000
```

Debug mode is controlled by `FLASK_DEBUG` env var (defaults to off).

## Route Structure

| Route | Level | Method |
|---|---|---|
| `/` | Redirects to Level 1 | GET |
| `/level1` | Level 1 - drag-and-drop game | GET, POST |
| `/level2_69` | Level 2 - riddle quiz | GET, POST |
| `/level3_nig` | Level 3 - five doors game | GET, POST |
| `/level4` | Completion page | GET |

Note: Route paths have non-standard suffixes. When templates use form actions, they should use `{{ url_for('functionName') }}` (e.g. `url_for('level3')`) rather than hardcoding the path.

## Testing Each Level

### Level 1 (Drag-and-Drop)
- Drag the plane image onto the tower (mole1) to trigger the first round
- Click "17 Minutes Later" to start round 2
- Drag plane onto second tower (mole2) to complete
- Click through the final form to POST and advance
- Key thing to verify: drag-and-drop JS functions use consistent parameter names

### Level 2 (Riddle Quiz)
- Answer riddles sequentially; answers are case-insensitive (uppercased)
- Click the success image to advance to next riddle
- After all riddles, a form appears to POST and advance
- Key thing to verify: `currentStep` bounds checking, riddle count display

### Level 3 (Five Doors)
- Click doors 1-4 to see "wrong door" images; close overlay each time
- Door 5 triggers a video; after video ends, "THE END" button appears
- The form POSTs to advance to Level 4
- Key thing to verify: video autoplay `.catch()` handling, form action uses `url_for`

## Error Handling Verification

- Visit any invalid URL (e.g. `/nonexistent`) to test the custom 404 handler
- Check browser console for JS errors during gameplay (especially drag events)
- Verify `Debug mode: off` in server startup output (unless FLASK_DEBUG=true)

## Shell-Based Quick Checks

```bash
# Verify 404 handler
curl -s http://localhost:5000/nonexistent
# Should return: <h1>404 — Page Not Found</h1>...

# Verify form action on Level 3
curl -s http://localhost:5000/level3_nig | grep -o 'action="[^"]*"'
# Should return: action="/level3_nig"

# Verify dynamic riddle count
curl -s http://localhost:5000/level2_69 | grep -o 'riddles.length'
# Should appear (not hardcoded "of 10")
```

## Devin Secrets Needed

None required - the app runs locally without authentication.
