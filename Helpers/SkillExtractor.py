import requests
import json

text_analytics_endpoint = "https://texttestshe23.cognitiveservices.azure.com/text/analytics/v3.0/entities/recognition/general"
api_key = "93b19f101a704911922048fae81a4254"

headers = {'Ocp-Apim-Subscription-Key' : api_key}

body = {
  "documents": [
    {
      "language": "en",
      "id": "1",
      "text": "feedback"
    },
  ]
}
body_str = json.dumps(body)

def extract_skills(feedback):
    body_request = body_str.replace("feedback",feedback)
    print(body_request)
    response = requests.post(text_analytics_endpoint,headers = headers,data=body_request)
    print(response.text)
    return response.text
