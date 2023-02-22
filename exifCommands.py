from PIL import Image, ExifTags
from PIL.ExifTags import TAGS

def read_exif(im):
    info = im._getexif()
    output = {}
    for key, value in info.items():
        output[TAGS.get(key, key)] = value

    return output

# TODO: write code here:
def write_exif(im, **kwargs):
    for tag in kwargs:
        pass