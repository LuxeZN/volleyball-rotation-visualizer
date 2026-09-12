from django.test import TestCase
from django.urls import reverse


class RotationVisualizerTests(TestCase):
    def test_rotation_visualizer_loads(self):
        response = self.client.get(reverse("visualizer:rotation_visualizer"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "visualizer/index.html")

    def test_rotation_systems_provided_to_template(self):
        response = self.client.get(reverse("visualizer:rotation_visualizer"))

        self.assertEqual(response.context["default_system"], "5-1")
        self.assertEqual(response.context["default_rotation"], "r1")
        self.assertEqual(response.context["default_state"], "serve")
        self.assertIn("5-1", response.context["rotation_systems"])
        self.assertIn("6-2", response.context["rotation_systems"])

    def test_opposite_players_are_mirrored_across_the_court(self):
        response = self.client.get(reverse("visualizer:rotation_visualizer"))
        serve_players = response.context["rotation_systems"]["5-1"]["rotations"][0]["states"]["serve"]["players"]
        by_number = {player["number"]: player["name"] for player in serve_players}

        self.assertEqual(by_number[1], "Outside 1")
        self.assertEqual(by_number[4], "Outside 2")
        self.assertEqual(by_number[2], "Setter")
        self.assertEqual(by_number[5], "Opposite")
        self.assertEqual(by_number[3], "Middle 1")
        self.assertEqual(by_number[6], "Middle 2")
