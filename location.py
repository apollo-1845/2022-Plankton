"""Functions for getting ISS location"""

from orbit import ISS

# import csv


# def save_to_csv(data, path):
#     with open("ISSPositions.csv", "a") as f:
#         writer = csv.writer(f)
#         writer.writerow(data)
#
# def save_location():
#     save_to_csv(get_location(), "csvTest.csv")

def convert_to_exif(angle):
    """Convert an angle from skyfield's format to (EXIF's (degrees, minutes 10*seconds), is it in reverse direction?)"""
    sign, degrees, minutes, seconds = angle.signed_dms()
    angle = f'{degrees:.0f}/1,{minutes:.0f}/1,{seconds*10:.0f}/10'
    return sign < 0, angle

def get_location():
    """Return ({W true, E false}, latitude, {S true, N false}, longitude), EXIF-encoded"""
    loc = ISS.location()
    return convert_to_exif(loc.latitude) + convert_to_exif(loc.longitude)
