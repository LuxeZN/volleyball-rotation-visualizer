from django.test import TestCase
from django.urls import reverse

from .views import ROTATION_STATES


class RotationVisualizerTests(TestCase):
    def test_rotation_visualizer_loads(self):
        response = self.client.get(reverse("visualizer:rotation_visualizer"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "visualizer/index.html")

    def test_rotation_states_provided_to_template(self):
        response = self.client.get(reverse("visualizer:rotation_visualizer"))

        self.assertEqual(response.context["rotation_states"], ROTATION_STATES)
        self.assertEqual(response.context["default_state"], "serve")
        self.assertEqual(len(ROTATION_STATES), 4)
        for state in ROTATION_STATES.values():
            self.assertEqual(len(state["players"]), 6)
