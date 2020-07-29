import requests
import json
import pprint 
import random

from Helpers.Classes import Place

bing_maps_key = "AoUmJwkCEO-LcuZPDFTJQrxCWMp6su1ujEntp66HHnL_TZpQWxGl1MoiHAGwzWVi"
locations_endpoint = "https://dev.virtualearth.net/REST/v1/LocalSearch/?type={type}&userLocation={point}&key={BingMapsAPIKey}"

def getLocalInfo(entityType,ulatitude,ulongitude):
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

    endpoint = locations_endpoint.format(type=entityType_api,point=point,BingMapsAPIKey=bing_maps_key)

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
        numPeople_ = random.uniform(0.5,3)

        placeObj = Place.place(name_,latitude_,longitude_,numPeople_,number_)
        places.append(placeObj)

    places_json = json.dumps([plac.__dict__ for plac in places])

    pprint.pprint(places_json)

    return places_json

if __name__ == '__main__': 
    getLocalInfo("recreation",47.602038,-122.333964)