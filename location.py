"""Functions for getting ISS location"""

from orbit import ISS

import pandas as pd


def save_to_csv(data, path):
    pd.DataFrame(data).to_csv(path, header=False)


def save_location():
    save_to_csv(get_location(), "csvTest.csv")


def get_location():
    return ISS.location()
