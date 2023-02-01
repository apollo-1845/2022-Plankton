from orbit import ISS

import json
import time

while True:
    location = ISS.location()

    positions = json.load(open("ISSPositions.json", "r"))
    positions[str(time.time())] = location
    json.dump(positions, open("ISSPositions.json", "w"))

    time.sleep(2)
