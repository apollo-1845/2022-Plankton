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

# def convert_to_exif(angle):
#     """Convert an angle from skyfield's format to (EXIF's (degrees, minutes 10*seconds), is it in reverse direction?)"""
#     sign, degrees, minutes, seconds = angle.signed_dms()
#     angle = (degrees, minutes, seconds)
#     return sign < 0, angle

def get_location():
    """Return (latitude, longitude), units: degrees"""
    loc = ISS.coordinates()
    return loc.latitude.degrees, loc.longitude.degrees
