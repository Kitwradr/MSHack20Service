import requests
import json
import pprint
import random
import os

dirname = os.path.dirname(__file__)


def getUS():
    """
    returns covid stats
    """

    stateWise = os.path.join(dirname, '../data/statewise.json')

    with open(stateWise) as f:
        data_states = json.load(f)
	
    return json.dumps(list(data_states))


if __name__ == "__main__":
    getUS()
