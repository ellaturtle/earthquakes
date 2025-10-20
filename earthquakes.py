import requests
import json
import os
from datetime import datetime

def get_data():
    response = requests.get(
        "http://earthquake.usgs.gov/fdsnws/event/1/query.geojson",
        params={
            'starttime': "2000-01-01",
            "maxlatitude": "58.723",
            "minlatitude": "50.008",
            "maxlongitude": "1.67",
            "minlongitude": "-9.756",
            "minmagnitude": "1",
            "endtime": "2018-10-11",
            "orderby": "time-asc"
        }
    )

    text = response.text

    #with open('earthquakes.json', 'w') as f:
       # f.write(text)

    data = json.loads(text)
    return data

def count_earthquakes(data):
    return data["metadata"]["count"]


def get_magnitude(earthquake):
    return earthquake["properties"]["mag"]


def get_location(earthquake):
    lon, lat, _ = earthquake["geometry"]["coordinates"]
    return (lat, lon)


def get_maximum(data):
    earthquakes = data["features"]
    max_earthquake = max(earthquakes, key=get_magnitude)  
    max_magnitude = get_magnitude(max_earthquake)
    max_location = get_location(max_earthquake)
    return max_magnitude, max_location

def get_year(earthquake):
    date = earthquake["properties"]["time"]
    # convert from ISO format to year
    year = datetime.utcfromtimestamp(date / 1000).year
    return year