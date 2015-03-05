import urllib   # urlencode function
import urllib2  # urlopen function (better than urllib version)
import json
from pprint import pprint


# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"


def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """

    f = urllib2.urlopen(url)
    response_text = f.read()
    response_data = json.loads(response_text)
    
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

    address = str(get_json(url))
    
    letter = 0
    letter1 = 0

    #stripping out the pieces of the google API code that we actually need

    while address[letter-3:letter].find('lat')  == -1:
        letter += 1
    while address[letter1-3:letter1].find('lng')  == -1:
        letter1 += 1

    if address[letter+3] != '-' and address[letter1+3] != '-':
        lat = address[letter+3:letter+12]
        lon = address[letter1+3:letter1+12]

    elif address[letter+3] == '-' and address[letter1+3] != '-':
        lat = address[letter+3:letter+13]
        lon = address[letter1+3:letter1+12]

    elif address[letter+3] != '-' and address[letter1+3] == '-':
        lat = address[letter+3:letter+12]
        lon = address[letter1+3:letter1+13]

    else:
        lat = address[letter+3:letter+13]
        lon = address[letter1+3:letter1+13]

    #returning the stripped-out latitude and longitudes of the place
    coordinates = [lat,lon]

    return coordinates

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    #we're now putting the latidue and longitude in the format that will allow us to search it with the MBTA API 
    url = 'http://realtime.mbta.com/developer/api/v2/stopsbylocation?api_key=wX9NwuHnZU2ToO7GmGR9uw&lat='+latitude+'&lon='+longitude+'&format=json'
    address = str(get_json(url))


    #initializing counters to strip out relevant information
    letter = 0
    letter1 = 0
    letter2 = 0

    while address[letter-11:letter].find('distance')  == -1:
        letter += 1
    while address[letter1-3:letter1].find('}, ')  == -1:
        letter1 += 1
    address_strip = address[letter:letter1]
    
    while address_strip[letter2-9:letter2].find('stop_name')  == -1:
        letter2 += 1

    return 'Stop Name: ' + address_strip[letter2+5:-4] + '   Distance: ' + address[letter+5:letter+15]


def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the 
    distance from the given place to that stop.
    """
    lat = get_lat_long(place_name)[0]
    lon = get_lat_long(place_name)[1]
    return get_nearest_station(lat,lon)

print find_stop_near('Museum of fine art')
