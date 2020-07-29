import requests
import json
import pprint
import random

from math import cos, asin, sqrt, pi, exp

from Helpers.Classes import Place

bing_maps_key = "AoUmJwkCEO-LcuZPDFTJQrxCWMp6su1ujEntp66HHnL_TZpQWxGl1MoiHAGwzWVi"
locations_endpoint = "https://dev.virtualearth.net/REST/v1/LocalSearch/?type={type}&userLocation={point}&key={BingMapsAPIKey}"


def distance(lat1, lon1, lat2, lon2):
    p = pi/180
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * \
        cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return 12742 * asin(sqrt(a))


def getLocalInfo(entityType, ulatitude, ulongitude):
    """
    returns a list of nearby stores based on user location
    """
    point = str(ulatitude)+','+str(ulongitude)
    if(entityType == "stores"):
        entityType_api = "MallsAndShoppingCenters"
    elif(entityType == "recreation"):
        entityType_api = "AmusementParks,Parks,Casinos,Zoos"
    elif(entityType == "eat"):
        entityType_api = "EatDrink"

    endpoint = locations_endpoint.format(
        type=entityType_api, point=point, BingMapsAPIKey=bing_maps_key)

    response = requests.get(endpoint)
    response_json = json.loads(response.text)

    resources = response_json["resourceSets"][0]["resources"]
    places = []
    for place in resources:
        point = place["point"]["coordinates"]
        latitude_ = point[0]
        longitude_ = point[1]
        name_ = place["name"]
        number_ = place["PhoneNumber"]
        numPeople_ = random.uniform(0.2, 3)
        distance_ = distance(float(ulatitude), float(ulongitude), latitude_, longitude_)
        score_ = exp(1/numPeople_)/distance_

        placeObj = Place.place(
            name_, latitude_, longitude_, numPeople_, distance_, number_, score_)

        places.append(placeObj)

    places.sort(key=lambda x: x.score, reverse=True)

    places_json = json.dumps([plac.__dict__ for plac in places])

    return places_json


if __name__ == '__main__':
    getLocalInfo("recreation", 47.602038, -122.333964)
