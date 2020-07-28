import requests
import json
import pprint 

bing_maps_key = "AoUmJwkCEO-LcuZPDFTJQrxCWMp6su1ujEntp66HHnL_TZpQWxGl1MoiHAGwzWVi"
locations_endpoint = "https://dev.virtualearth.net/REST/v1/LocalSearch/?query={query}&userLocation={point}&key={BingMapsAPIKey}"

def getLocalInfo():
    """
    returns a list of nearby stores based on user location
    """
    point = "47.602038,-122.333964"
    query = "grocery stores"
    endpoint = locations_endpoint.format(query=query,point=point,BingMapsAPIKey=bing_maps_key)

    response = requests.get(endpoint)

    pprint.pprint(json.loads(response.text))

if __name__ == '__main__': 
    getLocalInfo()