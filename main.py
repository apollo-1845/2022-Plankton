# Plankton's ISS Code Entrypoint

from datetime import datetime, timedelta
import time
from PIL import Image

import cv2

from camera import Camera
from location import get_location
from photoProcessing import remove_camera_cover, is_night

PROGRAM_TIME = timedelta(seconds=30) # TODO Update
MAX_CYCLE_SECONDS = 8

def run_iteration(i:int, camera:Camera):
    """Run one iteration of the program; return True if successful and should increment file-naming counter"""
    photo = camera.get_photo()

    photo = remove_camera_cover(photo)
    if(is_night(photo)):
        print("NIGHT")
        return False

    filename = f"data/{i}.tif"
    cv2.imwrite(filename, photo) # PNG is not supported by exif (BUT I THINK JPEG IS LOSSY!)

    # Add metadata
    pil_img = Image.open(filename)
    photo_tags = pil_img.tag_v2

    # Add timestamp
    dt = datetime.now()
    photo_tags[306] = f"{dt.year}:{dt.month}:{dt.day} {dt.hour}:{dt.minute}:{dt.second}"

    # Add ISS location
    lat, long = get_location()
    # # For testing only
    # lat, long = (i, -i/2)

    photo_tags[270] = f"{lat} {long}" # Custom Image Description

    print(photo_tags)
    pil_img.save(filename, tiffinfo=photo_tags)

    return True


PROGRAM_TIME_MINUS_ONE_CYCLE = PROGRAM_TIME-timedelta(seconds=MAX_CYCLE_SECONDS)

# Main loop
start = datetime.now()
now = datetime.now()

camera = Camera()

i = 0

while(now < start + PROGRAM_TIME_MINUS_ONE_CYCLE):
    print(i, now-start)
    # try:
    successful = run_iteration(i, camera)
    if(successful): i += 1
    # except Exception as err:
    #     print("ERROR", err)
    #     pass # and ignore error
    now = datetime.now()
print("Ended in", now-start)