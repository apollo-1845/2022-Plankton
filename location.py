"""Functions for getting ISS location"""

from orbit import ISS

def get_location():
    return ISS.location()
