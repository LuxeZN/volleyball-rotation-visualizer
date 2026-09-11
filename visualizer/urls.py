from django.urls import path

from .views import rotation_visualizer

app_name = "visualizer"

urlpatterns = [
    path("", rotation_visualizer, name="rotation_visualizer"),
]
