import cv2
import numpy as np
"""Functions to process images, using OpenCV"""

IMAGE_SHAPE_NP = (1944, 2592, 3)
COVER_CENTRE = (2592//2, 1944//2)
COVER_RADIUS = 1944//2

CAMERA_COVER_MASK = np.zeros(IMAGE_SHAPE_NP[:2], dtype="uint8")
CAMERA_COVER_MASK = cv2.circle(CAMERA_COVER_MASK, COVER_CENTRE, COVER_RADIUS, 255, -1)

# print("COVER", CAMERA_COVER_MASK.dtype, CAMERA_COVER_MASK.shape)
def remove_camera_cover(image):
    # print("IMG", image.dtype, image.shape)
    return cv2.bitwise_and(image, image, mask=CAMERA_COVER_MASK) # * CAMERA_COVER_MASK

def is_night(image):
    # print("MAX", np.max(image))
    return np.max(image) < 100