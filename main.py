from flask import Flask, request
from flask_cors import CORS
import json
import os

from Helpers.LocalInfo import getLocalInfo

app = Flask(__name__)
CORS(app)

@app.route('/')
def main_func():
  return 'Hello Flask, on Azure App Service for Linux!'

@app.route('/local_info',methods=['GET'])
def get_local():

  lattitude = request.args.get('lattitude')
  longitude = request.args.get('longitude')
  entityType = request.args.get('entityType')

  response = getLocalInfo(entityType,lattitude,longitude)
  return response

if __name__ == '__main__':                 
  app.run(host="0.0.0.0", port=5001, debug=True)