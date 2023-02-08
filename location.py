"""Functions for getting ISS location"""

from orbit import ISS

import csv


def save_to_csv(data, path):
    with open("ISSPositions.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow(data)

def save_location():
    save_to_csv(get_location(), "csvTest.csv")


def get_location():
    return ISS.location()
