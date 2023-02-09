import cv2
from time import sleep

# Press ENTER to toggle preview

from camera import Camera # For fake camera only

cam = Camera()

print("""---
Please click this console.
Then, press ENTER to toggle the image preview.
---""")

sleep(3)

while True:
    img = cam.get_photo()
    
    cam.start_preview()
    
    # cam.test_brightness()

    input()

    cam.stop_preview()
    
    input("ENTER TO ENTER PREVIEW")