# tle_loader.py
import requests
from skyfield.api import load, EarthSatellite

def load_satellite_from_celestrak(name, url="https://celestrak.com/NORAD/elements/stations.txt"):
    r = requests.get(url)
    lines = r.text.splitlines()
    for i, line in enumerate(lines):
        if name in line:
            line1 = lines[i+1]
            line2 = lines[i+2]
            ts = load.timescale()
            return EarthSatellite(line1, line2, name, ts)
    return None