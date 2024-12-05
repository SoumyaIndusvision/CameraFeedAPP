import cv2
import logging
from django.http import StreamingHttpResponse, HttpResponse

# Set up logging for debugging
logger = logging.getLogger(__name__)

def stream_camera_feed(camera):
    try:
        # Construct the RTSP URL using the camera's credentials
        camera_url = f"rtsp://{camera.username}:{camera.password}@{camera.ip_address}:{camera.port}"
        
        # Open the camera feed using OpenCV
        cap = cv2.VideoCapture(camera_url)
        
        if not cap.isOpened():
            logger.error(f"Unable to connect to camera at {camera_url}")
            raise ValueError("Unable to connect to the camera feed.")
        
        # Function to stream the video as MJPEG
        def generate():
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                # Encode the frame to JPEG
                _, jpeg = cv2.imencode('.jpg', frame)
                frame = jpeg.tobytes()
                
                # Yield the frame as MJPEG stream
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        
        return StreamingHttpResponse(generate(), content_type='multipart/x-mixed-replace; boundary=frame')
    
    except Exception as e:
        logger.error(f"Error while streaming camera feed: {str(e)}")
        return HttpResponse(f"Error: {str(e)}", status=500)
