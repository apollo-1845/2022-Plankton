"""[FAKE] Functions for getting camera data"""

import requests
import numpy as np
import cv2
class Camera():
    """A camera with the same methods as the actual Camera which uses online demo data"""

    image_id = 150
    image = None

    def __init__(self):
        """Initialise the fake camera"""
        pass

    def set_image_id(self, id:int):
        """Set the image as a certain ID from https://github.com/raspberrypilearning/astropi-ndvi/tree/master/en/resources/"""
        self.image_id = id


    def get_photo(self):
        # Get image link
        url = f"https://github.com/raspberrypilearning/astropi-ndvi/blob/master/en/resources/cslab3ogel_Files_RawData_raw_image_{self.image_id}.jpeg?raw=true"

        # Request data from dataset
        with requests.get(url) as r:
            byte_resp = r.content

        # Next photo next time
        self.image_id += 1
        self.image_id %= 250

        # Turn into CV2 image and return
        array_resp = np.array(list(byte_resp), np.uint8)
        return cv2.imdecode(array_resp, cv2.IMREAD_UNCHANGED)