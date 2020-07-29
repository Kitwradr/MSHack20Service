import requests
import json
import pprint 

bing_maps_key = "AoUmJwkCEO-LcuZPDFTJQrxCWMp6su1ujEntp66HHnL_TZpQWxGl1MoiHAGwzWVi"
locations_endpoint = "https://dev.virtualearth.net/REST/v1/LocalSearch/?type={type}&userLocation={point}&key={BingMapsAPIKey}"

def getLocalInfo(entityType,lattitude,longitude):
    """
    returns a list of nearby stores based on user location
    """
    point = str(lattitude)+','+str(longitude)
    if(entityType == "stores"):
        entityType_api = "MallsAndShoppingCenters"
    elif(entityType == "recreation"):
        entityType_api = "AmusementParks,Parks,Casinos,Zoos"
    elif(entityType == "eat"):
        entityType_api = "EatDrink"

    endpoint = locations_endpoint.format(type=entityType_api,point=point,BingMapsAPIKey=bing_maps_key)

    response = requests.get(endpoint)
    response_json = json.loads(response.text)
    pprint.pprint(response_json)

    return response_json

if __name__ == '__main__': 
    getLocalInfo("recreation",47.602038,-122.333964)