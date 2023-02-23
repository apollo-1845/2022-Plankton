"""Functions to process images, using OpenCV"""
import cv2
import numpy as np

IMAGE_SHAPE_NP = (1944, 2592, 3)
COVER_CENTRE = (2592//2, 1944//2)
COVER_RADIUS = 1944//2

CAMERA_COVER_MASK = np.zeros(IMAGE_SHAPE_NP[:2], dtype="uint8")
CAMERA_COVER_MASK = cv2.circle(CAMERA_COVER_MASK, COVER_CENTRE, COVER_RADIUS, 255, -1)

def remove_camera_cover(image):
    """Set the camera cover region of the image to 0 so it reduces the filesize with compression and removes irrelevant data"""
    return cv2.bitwise_and(image, image, mask=CAMERA_COVER_MASK)

def is_night(image):
    """Return True if the image is dark and therefore useless."""
    return np.max(image) < 100