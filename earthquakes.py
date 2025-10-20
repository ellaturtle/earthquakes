import requests
import json
import os
print("Current working directory:", os.getcwd())


# see week 4 prep original to see # comments 

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
data = get_data()

def count_earthquakes(data):
    return data["metadata"]["count"]

num_eq = count_earthquakes(data)
print(f'There are {num_eq} earthquakes.')


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


print(f"Loaded {count_earthquakes(data)}")
max_magnitude, max_location = get_maximum(data)
print(f"The strongest earthquake was at {max_location} with magnitude {max_magnitude}")