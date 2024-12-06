from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Camera
from .streaming import stream_camera_feed
from .serializers import CameraSerializer

class CameraStreamView(APIView):
    @swagger_auto_schema(
        operation_description="Stream a live camera feed by camera ID",
        responses={
            200: openapi.Response('Success'),
            404: openapi.Response('Camera not found')
        },
        manual_parameters=[
            openapi.Parameter(
                'camera_id',
                openapi.IN_PATH,
                description="ID of the camera to stream",
                type=openapi.TYPE_INTEGER
            )
        ]
    )
    def get(self, request, camera_id, *args, **kwargs):
        try:
            camera = Camera.objects.get(id=camera_id)
            return stream_camera_feed(camera)
        except Camera.DoesNotExist:
            return Response({"error": "Camera not found"}, status=status.HTTP_404_NOT_FOUND)

class CameraListView(ListAPIView):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer

    @swagger_auto_schema(
        operation_description="Retrieve a list of all cameras",
        responses={200: CameraSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
