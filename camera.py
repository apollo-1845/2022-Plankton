"""Functions for getting camera data"""

from picamera import PiCamera
import picamera.array

from time import sleep

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
    
    def start_preview(self):
        self.camera.start_preview()
        
    def test_brightness(self):
        for brightness in range(100):
            self.camera.annotate_text = "Brightness %s" % brightness
            self.camera.brightness = brightness
            sleep(0.1)
        
    def stop_preview(self):
        self.camera.stop_preview()