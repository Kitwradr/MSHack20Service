import datetime
from flask import Flask, request
from flask_cors import CORS
import json
import os

from Helpers.LocalInfo import getLocalInfo
from Helpers.USstates import getUS
from Helpers.SkillExtractor import extract_skills
from Helpers.DataAccess import store_feedback_skills

app = Flask(__name__)
CORS(app)


@app.route('/')
def main_func():
    return 'Hello Flask, on Azure App Service for Linux! '+ str(datetime.datetime.now())


@app.route('/local_info', methods=['GET'])
def get_local():

    lattitude = request.args.get('lattitude')
    longitude = request.args.get('longitude')
    entityType = request.args.get('entityType')

    response = getLocalInfo(entityType, lattitude, longitude)

    return response


@app.route('/covid_us', methods=['GET'])
def get_covid_us():
	return getUS()

@app.route('/hackhr/get_skills', methods=['POST'])
def get_skills():
    body = request.json
    feedbact_str = body['feedback']
    return extract_skills(feedbact_str)

@app.route('/hackhr/store_data', methods=['POST'])
def store_data():

    body = request.json
    hm_id = body['hm_id']
    job_id = body['job_id']
    candidate_id = body['candidate_id']
    skills_scores = body['skills_scores']
    recommendation = body['recommendation']
    org = body['org']
    store_feedback_skills(job_id,hm_id,candidate_id,skills_scores,recommendation,org)

    return "Executed"

        


@app.route('/hackhr/get_data', methods=['GET'])
def get_data():
    body = request.json
    hm_id = body["hm_id"]
    org = body["org"]
    result = body["Result"]



	

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
