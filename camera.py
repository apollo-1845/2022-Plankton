"""Functions for getting camera data"""

from picamera import PiCamera
import picamera

class Camera():
    """A camera that captures numpy-array images with """
    def __init__(self):
        """Initialise the camera"""
        self.camera = PiCamera()

    def get_photo(self):
        """Capture a photo and return it as a BGR numpy array"""
        stream = picamera.array.PiRGBArray(self.camera)
        self.camera.capture(stream, format="bgr", use_video_port=True)
        return stream.array