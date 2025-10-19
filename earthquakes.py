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
    ###"""Retrive the magnitude of an earthquake item."""
    ###return ...


###def get_location(earthquake):
   ### """Retrieve the latitude and longitude of an earthquake item."""
    # There are three coordinates, but we don't care about the third (altitude)
    ###return ...


###def get_maximum(data):
  ###  """Get the magnitude and location of the strongest earthquake in the data."""
    ###...


# With all the above functions defined, we can now call them and get the result
#data = get_data()
#print(f"Loaded {count_earthquakes(data)}")
#max_magnitude, max_location = get_maximum(data)
#print(f"The strongest earthquake was at {max_location} with magnitude {max_magnitude}")