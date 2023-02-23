"""Test opening TIFF files, opening them and displaying metadata"""
import datetime
from PIL import Image

filename = "data/0.tif"

# Open w/ PIL for metadata
pil_img = Image.open(filename)
photo_tags = pil_img.tag_v2

dt_raw = photo_tags[306]
date_raw, time_raw = dt_raw.split()
year_raw, month_raw, day_raw = date_raw.split(":")
hour_raw, min_raw, sec_raw = time_raw.split(":")
timestamp = datetime.datetime(int(year_raw), int(month_raw), int(day_raw), int(hour_raw), int(min_raw), int(sec_raw))

coords_raw = photo_tags[270] # Image Description, repurposed as cannot set custom tags

lat, long = map(float, coords_raw.split())

print(f"TIME {timestamp} LAT {lat} LONG {long}")