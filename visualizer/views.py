from django.shortcuts import render


ROTATION_STATES = {
    "serve": {
        "label": "Serve (5-1)",
        "players": [
            {"name": "Setter", "number": 1, "x": 510, "y": 255},
            {"name": "Opposite", "number": 2, "x": 510, "y": 55},
            {"name": "Middle 1", "number": 3, "x": 310, "y": 55},
            {"name": "Outside 1", "number": 4, "x": 110, "y": 55},
            {"name": "Middle 2", "number": 5, "x": 110, "y": 255},
            {"name": "Outside 2", "number": 6, "x": 310, "y": 255},
        ],
    },
    "serve_receive": {
        "label": "Serve-Receive",
        "players": [
            {"name": "Setter", "number": 1, "x": 470, "y": 190},
            {"name": "Opposite", "number": 2, "x": 500, "y": 65},
            {"name": "Middle 1", "number": 3, "x": 310, "y": 70},
            {"name": "Outside 1", "number": 4, "x": 125, "y": 95},
            {"name": "Middle 2", "number": 5, "x": 295, "y": 220},
            {"name": "Outside 2", "number": 6, "x": 125, "y": 220},
        ],
    },
    "first_touch_us": {
        "label": "After First Touch (Our Side)",
        "players": [
            {"name": "Setter", "number": 1, "x": 305, "y": 120},
            {"name": "Opposite", "number": 2, "x": 500, "y": 70},
            {"name": "Middle 1", "number": 3, "x": 305, "y": 55},
            {"name": "Outside 1", "number": 4, "x": 115, "y": 80},
            {"name": "Middle 2", "number": 5, "x": 305, "y": 255},
            {"name": "Outside 2", "number": 6, "x": 120, "y": 235},
        ],
    },
    "first_touch_them": {
        "label": "After First Touch (Opponent Side)",
        "players": [
            {"name": "Setter", "number": 1, "x": 505, "y": 230},
            {"name": "Opposite", "number": 2, "x": 505, "y": 100},
            {"name": "Middle 1", "number": 3, "x": 285, "y": 105},
            {"name": "Outside 1", "number": 4, "x": 145, "y": 105},
            {"name": "Middle 2", "number": 5, "x": 290, "y": 235},
            {"name": "Outside 2", "number": 6, "x": 145, "y": 235},
        ],
    },
}


def rotation_visualizer(request):
    return render(
        request,
        "visualizer/index.html",
        {
            "rotation_states": ROTATION_STATES,
            "default_state": "serve",
        },
    )
