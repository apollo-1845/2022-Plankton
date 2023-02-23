"""PLANKTON Astro Pi 2022: ISS Code
---
We plan to complete most of the analysis on Earth so:
(1) There is a lower risk of our code running into a bug on the ISS
(2) We can analyse different algorithms on Earth based on our previous results and hypotheses.
This code:
(1) Uses the PiCamera to photograph an image of Earth
(2) Removes the camera cover and any photos with too little light (implying it is night)
(3) Calculates the date, time and ISS location and saves them as TIFF tags
(4) Saves the photos captured with the tags as .tif files, losslessly compressed.
"""

from datetime import datetime, timedelta
import time
from PIL import Image

import cv2

from camera import Camera
from location import get_location
from photoProcessing import remove_camera_cover, is_night

PROGRAM_TIME = timedelta(hours=3) # Program only runs in three-hour window
MAX_CYCLE_SECONDS = 18

def run_iteration(i:int, camera:Camera):
    """Run one iteration of the program; return True if successful and should increment file-naming counter"""
    photo = camera.get_photo()

    photo = remove_camera_cover(photo)
    if(is_night(photo)):
        print("NIGHT")
        return False

    filename = f"data/{i}.tif"
    cv2.imwrite(filename, photo)

    # Add metadata
    pil_img = Image.open(filename)
    photo_tags = pil_img.tag_v2

    # Add timestamp
    dt = datetime.now()
    photo_tags[306] = f"{dt.year}:{dt.month}:{dt.day} {dt.hour}:{dt.minute}:{dt.second}"

    # Add ISS location
    lat, long = get_location()

    photo_tags[270] = f"{lat} {long}" # Custom Image Description w/ location

    print(photo_tags)
    pil_img.save(filename, tiffinfo=photo_tags)

    return True


PROGRAM_TIME_MINUS_ONE_CYCLE = PROGRAM_TIME-timedelta(seconds=MAX_CYCLE_SECONDS)

# Main loop
start = datetime.now()
now = datetime.now()

camera = Camera()

i = 0

while(last_iteration_time < start + PROGRAM_TIME_MINUS_ONE_CYCLE):
    print(i, last_iteration_time-start)
    try:
        successful = run_iteration(i, camera)
        if(successful): i += 1
    except Exception as err:
        print("ERROR", err)
        pass # and ignore error
    while(datetime.now() < last_iteration_time + timedelta(seconds=18)):
        # Every 18 seconds, new iteration
        time.sleep(0.2)
    last_iteration_time = datetime.now()
print("Ended in", now-start)
