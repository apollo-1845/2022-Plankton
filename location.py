"""Functions for getting ISS location"""

from orbit import ISS

def get_location():
    """Return (latitude, longitude), units: degrees"""
    loc = ISS.coordinates()
    return loc.latitude.degrees, loc.longitude.degrees
