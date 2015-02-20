"""
Geocoding and Web APIs Project Toolbox exercise

Find the MBTA stops closest to a given location.

Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""

import urllib   # urlencode function
import urllib2  # urlopen function (better than urllib version)
import json
from pprint import pprint


# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"


# A little bit of scaffolding if you want to use it
def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    import urllib2, json
    
    f = urllib2.urlopen(url)
    response_text = f.read()
    response_data = json.loads(response_text)

    response_data =  json.dumps([s['geometry'] for s in response_data['results']], indent=2)
    #how to find the actual latitude and longitude?
    #cannot find
    return response_data

def get_jsonMBTA(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    import urllib2, json
    
    f = urllib2.urlopen(url)
    response_text = f.read()
    response_data = json.loads(response_text)

    response_data =  json.dumps([s['geometry'] for s in response_data['results']], indent=2)
    #how to find the actual latitude and longitude?
    #cannot find
    return response_data

def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.

    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.

    >>>get_lat_long(4 Normandy Drive, Chadds Ford, PA, 19317)
    [
      {
        "location": {
          "lat": 39.86293999999999, 
          "lng": -75.652636
        }, 
        "viewport": {
          "northeast": {
            "lat": 39.8642889802915, 
            "lng": -75.6512870197085
          }, 
          "southwest": {
            "lat": 39.8615910197085, 
            "lng": -75.65398498029151
          }
        }, 
        "location_type": "ROOFTOP"
      }
    ]
    """
    #we're now putting the place_name in the format that will allow us to search it with Google's API    
    place_name = ((place_name.replace(" ","+"))).lower()
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + place_name
    return get_lat_long('4 Normandy Drive, Chadds Ford, PA, 19317')

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    #we're now putting the latidue and longitude in the format that will allow us to search it with the MBTA API 
    url = 'http://realtime.mbta.com/developer/api/v2/stopsbylocation?api_key=wX9NwuHnZU2ToO7GmGR9uw&lat='+latitude+'lon='+longitude+'&format=json'



get_nearest_station(42.364219, -71.053523)

def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the 
    distance from the given place to that stop.
    """
    pass

