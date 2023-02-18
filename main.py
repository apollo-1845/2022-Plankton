# Plankton's ISS Code Entrypoint

from datetime import datetime, timedelta
from time import sleep
from exif import Image

import cv2

from camera import Camera
from location import get_location

PROGRAM_TIME = timedelta(seconds=10)
MAX_CYCLE_SECONDS = 8

def run_iteration(i:int, camera:Camera):
    """Run one iteration of the program"""
    photo = camera.get_photo()
    filename = f"data/{i}.jpg"
    cv2.imwrite(filename, photo) # PNG is not supported by exif (BUT I THINK JPEG IS LOSSY!)

    # Add metadata
    with open(filename, 'rb') as photo_file:
        photo_tags = Image(photo_file.read())

    west, lat, south, long = get_location()
    photo_tags.gps_latitude = lat
    photo_tags.gps_latitude_ref = "W" if west else "E"
    photo_tags.gps_longitude = long
    photo_tags.gps_longitude_ref = "S" if south else "N"

    # # For testing only
    # photo_tags.gps_latitude = (i, i/10, i/100)
    # photo_tags.gps_latitude_ref = "W" if (i % 2 == 1) else "E"
    # photo_tags.gps_longitude = (i, i/10, i/100)
    # photo_tags.gps_longitude_ref = "S" if (i % 2 == 0) else "N"

    with open(filename, 'wb') as photo_file:
        photo_file.write(photo_tags.get_file())


PROGRAM_TIME_MINUS_ONE_CYCLE = PROGRAM_TIME-timedelta(seconds=MAX_CYCLE_SECONDS)

# Main loop
start = datetime.now()
now = datetime.now()

camera = Camera()

i = 0

while(now < start + PROGRAM_TIME_MINUS_ONE_CYCLE):
    print(now-start)
    try:
        run_iteration(i, camera)
    except:
        print("ERROR")
        pass # and ignore error
    i += 1
    now = datetime.now()
print("Ended in", now-start)