import cv2

from fake.camera import Camera # For fake camera only

cam = Camera()

while True:
    img = cam.get_photo()
    print(cam.image_id)
    if img.max() <= 100:
        # Don't show night images
        cam.image_id += 10
        continue
    # Display Image
    # Window name in which image is displayed
    window_name = 'image'

    # Using cv2.imshow() method
    # Displaying the image
    cv2.imshow(window_name, img)

    # waits for user to press any key
    # (this is necessary to avoid Python kernel form crashing)
    cv2.waitKey(0)

    # closing all open windows
    cv2.destroyAllWindows()