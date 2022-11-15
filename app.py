import json
import os
import requests
import time
import datetime
from sys import stderr
from flask import Flask, request, jsonify

app = Flask(__name__)

api_key = os.environ.get("API_KEY", "")
if api_key == "":
    print("api key is required", file=stderr)

api_base_url = "https://api.stagingv3.microgen.id/query/api/v1/" + api_key

@app.get("/dashbiard/metrics/cpu")
def metricscpu():
    d=str(datetime.datetime.now())
    p='%Y-%m-%d %H:%M:%S.%f'
    e = int(time.mktime(time.strptime(d,p)))
    x = str(e)
    url="http://10.10.65.1:8080/api/v1/clusters/sapujagad/hosts/sapujagad-master01.kayangan.com?fields=metrics/cpu&_="+x+""
    username = "sapujagad"
    password = "kayangan"
    response = requests.get(url, auth=(username, password))
    # print(response.status_code)
    return response.json()
    



if __name__ == "__main__":
    app.run(debug=True)
