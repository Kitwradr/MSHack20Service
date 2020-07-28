from flask import Flask, request
import json
import os

app = Flask(__name__)

@app.route('/')
def main_func():
  return 'Hello Flask, on Azure App Service for Linux!'

@app.route('/local_stores',methods=['GET'])
def get_local():
  point = 12.981480, 77.507180

if __name__ == '__main__':                 
  app.run(host="0.0.0.0", port=5001, debug=True)