import requests # lib for making http requests
import json

url = "https://flask-app-demo.onrender.com/predict?level=Junior&lang=Java&tweets=yes&phd=no"

response = requests.get(url=url)

# first thing check the response's status code
print(response.status_code)
if response.status_code == 200:
    # extract prediction from response's JSON text
    json_object = json.loads(response.text)
    print(json_object)