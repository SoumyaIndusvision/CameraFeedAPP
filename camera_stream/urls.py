from django.urls import path
from .views import CameraStreamView, CameraListView

urlpatterns = [
    path('camera/<int:camera_id>/stream/', CameraStreamView.as_view(), name='camera_stream'),
    path('cameras/', CameraListView.as_view(), name='camera_list'),
]
