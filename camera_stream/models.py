from django.db import models

class Camera(models.Model):
    name = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=15)  # IP address of the camera
    port = models.IntegerField(default=554)  # RTSP default port
    username = models.CharField(max_length=255)  # Login username for camera
    password = models.CharField(max_length=255)  # Login password for camera
    protocol = models.CharField(max_length=50, choices=[('rtsp', 'RTSP'), ('http', 'HTTP')], default='rtsp')

    def __str__(self):
        return self.name
