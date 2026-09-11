# volleyball-rotation-visualizer

A small Django app that visualizes volleyball rotations on a single-side court.

It currently supports both **5-1** and **6-2** systems, plus animated serve and serve-receive walkthroughs.

## Features

- System selector for **5-1** and **6-2**
- Rotation navigation for **Rotation 1** through **Rotation 6**
- State views for serve, serve-receive, and post-first-touch positioning
- Animated serve visualization that sends the ball over the net before the players transition
- Animated serve-receive visualization that brings the ball over the net to a passer, then shows the setter and hitters getting into attack shape
- Per-rotation custom serve targets
- Motion trails for both ball and player movement
- Position names shown inside each player circle, with an optional abbreviation toggle for mobile-friendly labels
- Centered, responsive layout for the court and controls

## Run locally

```bash
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open `http://127.0.0.1:8000/`.

## Notes

- The court is displayed as a single-side half court with the net at the top edge.
- The visual layouts are geared toward coaching/demo use rather than exact real-match tracking precision.
