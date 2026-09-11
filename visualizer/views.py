from django.shortcuts import render


def court_y(y):
    return round(65 + ((y - 55) * 0.75), 2)



SERVE_SPOTS = {
    1: {"x": 510, "y": 255},
    2: {"x": 510, "y": 55},
    3: {"x": 310, "y": 55},
    4: {"x": 110, "y": 55},
    5: {"x": 110, "y": 255},
    6: {"x": 310, "y": 255},
}


def build_base_state(players):
    return {
        "players": [
            {
                "name": player["name"],
                "number": player["number"],
                "x": player["x"],
                "y": court_y(player["y"]),
            }
            for player in players
        ]
    }


def rotated_number(start_number, steps):
    return ((start_number - 1 + steps) % 6) + 1


def get_rotation_animation(system_key, step):
    serve_targets = [
        {"x": 132, "y": 18},
        {"x": 150, "y": 20},
        {"x": 156, "y": 22},
        {"x": 120, "y": 21},
        {"x": 182, "y": 19},
        {"x": 105, "y": 19},
    ]
    receive_origins = [
        {"x": 530, "y": 18},
        {"x": 532, "y": 18},
        {"x": 526, "y": 18},
        {"x": 535, "y": 18},
        {"x": 540, "y": 18},
        {"x": 520, "y": 18},
    ]
    receiver_numbers = {
        "5-1": [4, 3, 6, 5, 4, 6],
        "6-2": [4, 3, 6, 5, 4, 6],
    }
    serve_net_cross = [
        {"x": 310, "y": 34},
        {"x": 310, "y": 34},
        {"x": 310, "y": 34},
        {"x": 310, "y": 34},
        {"x": 310, "y": 34},
        {"x": 310, "y": 34},
    ]
    receive_net_cross = [
        {"x": 310, "y": 34},
        {"x": 310, "y": 34},
        {"x": 310, "y": 34},
        {"x": 310, "y": 34},
        {"x": 310, "y": 34},
        {"x": 310, "y": 34},
    ]

    return {
        "serve_target": serve_targets[step],
        "serve_net_cross": serve_net_cross[step],
        "receive_origin": receive_origins[step],
        "receive_net_cross": receive_net_cross[step],
        "receiver_number": receiver_numbers.get(system_key, receiver_numbers["5-1"])[step],
    }


def build_rotations(system_key, base_states):
    base_players = base_states["serve"]["players"]
    initial_numbers = {player["name"]: player["number"] for player in base_players}
    base_state_number_coords = {
        state_key: {player["number"]: {"x": player["x"], "y": player["y"]} for player in state["players"]}
        for state_key, state in base_states.items()
    }

    rotations = []
    for step in range(6):
        rotation_states = {}
        for state_key, state in base_states.items():
            rotated_players = []
            for player in state["players"]:
                current_number = rotated_number(initial_numbers[player["name"]], step)
                coords = base_state_number_coords[state_key][current_number]
                rotated_players.append(
                    {
                        "name": player["name"],
                        "number": current_number,
                        "x": coords["x"],
                        "y": coords["y"],
                    }
                )

            rotation_states[state_key] = {
                "label": state["label"],
                "players": rotated_players,
            }

        rotations.append(
            {
                "key": f"r{step + 1}",
                "label": f"Rotation {step + 1}",
                "states": rotation_states,
                "animation": get_rotation_animation(system_key, step),
            }
        )

    return rotations


BASE_SYSTEMS = {
    "5-1": {
        "label": "5-1",
        "states": {
            "serve": {
                "label": "Serve",
                "players": [
                    {"name": "Setter", "number": 1, **SERVE_SPOTS[1]},
                    {"name": "Opposite", "number": 2, **SERVE_SPOTS[2]},
                    {"name": "Middle 1", "number": 3, **SERVE_SPOTS[3]},
                    {"name": "Outside 1", "number": 4, **SERVE_SPOTS[4]},
                    {"name": "Middle 2", "number": 5, **SERVE_SPOTS[5]},
                    {"name": "Outside 2", "number": 6, **SERVE_SPOTS[6]},
                ],
            },
            "serve_receive": {
                "label": "Serve-Receive",
                "players": [
                    {"name": "Setter", "number": 1, "x": 470, "y": court_y(190)},
                    {"name": "Opposite", "number": 2, "x": 500, "y": court_y(65)},
                    {"name": "Middle 1", "number": 3, "x": 310, "y": court_y(70)},
                    {"name": "Outside 1", "number": 4, "x": 125, "y": court_y(95)},
                    {"name": "Middle 2", "number": 5, "x": 295, "y": court_y(220)},
                    {"name": "Outside 2", "number": 6, "x": 125, "y": court_y(220)},
                ],
            },
            "first_touch_us": {
                "label": "After First Touch (Our Side)",
                "players": [
                    {"name": "Setter", "number": 1, "x": 305, "y": court_y(120)},
                    {"name": "Opposite", "number": 2, "x": 500, "y": court_y(70)},
                    {"name": "Middle 1", "number": 3, "x": 305, "y": court_y(55)},
                    {"name": "Outside 1", "number": 4, "x": 115, "y": court_y(80)},
                    {"name": "Middle 2", "number": 5, "x": 305, "y": court_y(255)},
                    {"name": "Outside 2", "number": 6, "x": 120, "y": court_y(235)},
                ],
            },
            "first_touch_them": {
                "label": "After First Touch (Opponent Side)",
                "players": [
                    {"name": "Setter", "number": 1, "x": 505, "y": court_y(230)},
                    {"name": "Opposite", "number": 2, "x": 505, "y": court_y(100)},
                    {"name": "Middle 1", "number": 3, "x": 285, "y": court_y(105)},
                    {"name": "Outside 1", "number": 4, "x": 145, "y": court_y(105)},
                    {"name": "Middle 2", "number": 5, "x": 290, "y": court_y(235)},
                    {"name": "Outside 2", "number": 6, "x": 145, "y": court_y(235)},
                ],
            },
        },
    },
    "6-2": {
        "label": "6-2",
        "states": {
            "serve": {
                "label": "Serve",
                "players": [
                    {"name": "Setter A", "number": 1, **SERVE_SPOTS[1]},
                    {"name": "Opposite A", "number": 2, **SERVE_SPOTS[2]},
                    {"name": "Middle 1", "number": 3, **SERVE_SPOTS[3]},
                    {"name": "Outside 1", "number": 4, **SERVE_SPOTS[4]},
                    {"name": "Middle 2", "number": 5, **SERVE_SPOTS[5]},
                    {"name": "Setter B", "number": 6, **SERVE_SPOTS[6]},
                ],
            },
            "serve_receive": {
                "label": "Serve-Receive",
                "players": [
                    {"name": "Setter A", "number": 1, "x": 470, "y": court_y(205)},
                    {"name": "Opposite A", "number": 2, "x": 490, "y": court_y(75)},
                    {"name": "Middle 1", "number": 3, "x": 305, "y": court_y(78)},
                    {"name": "Outside 1", "number": 4, "x": 130, "y": court_y(95)},
                    {"name": "Middle 2", "number": 5, "x": 295, "y": court_y(225)},
                    {"name": "Setter B", "number": 6, "x": 140, "y": court_y(225)},
                ],
            },
            "first_touch_us": {
                "label": "After First Touch (Our Side)",
                "players": [
                    {"name": "Setter A", "number": 1, "x": 305, "y": court_y(120)},
                    {"name": "Opposite A", "number": 2, "x": 500, "y": court_y(70)},
                    {"name": "Middle 1", "number": 3, "x": 305, "y": court_y(55)},
                    {"name": "Outside 1", "number": 4, "x": 115, "y": court_y(82)},
                    {"name": "Middle 2", "number": 5, "x": 305, "y": court_y(255)},
                    {"name": "Setter B", "number": 6, "x": 122, "y": court_y(236)},
                ],
            },
            "first_touch_them": {
                "label": "After First Touch (Opponent Side)",
                "players": [
                    {"name": "Setter A", "number": 1, "x": 505, "y": court_y(230)},
                    {"name": "Opposite A", "number": 2, "x": 505, "y": court_y(100)},
                    {"name": "Middle 1", "number": 3, "x": 285, "y": court_y(105)},
                    {"name": "Outside 1", "number": 4, "x": 145, "y": court_y(105)},
                    {"name": "Middle 2", "number": 5, "x": 290, "y": court_y(235)},
                    {"name": "Setter B", "number": 6, "x": 145, "y": court_y(235)},
                ],
            },
        },
    },
}


ROTATION_SYSTEMS = {
    system_key: {
        "label": system["label"],
        "rotations": build_rotations(system_key, system["states"]),
    }
    for system_key, system in BASE_SYSTEMS.items()
}
def rotation_visualizer(request):
    return render(
        request,
        "visualizer/index.html",
        {
            "rotation_systems": ROTATION_SYSTEMS,
            "default_system": "5-1",
            "default_rotation": "r1",
            "default_state": "serve",
        },
    )

