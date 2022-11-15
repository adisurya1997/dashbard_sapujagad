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

@app.get("/dashboard/metrics/cpu")
def metricscpu():
    d=str(datetime.datetime.now())
    p='%Y-%m-%d %H:%M:%S.%f'
    e = int(time.mktime(time.strptime(d,p))) - 3600
    x = str(e)
    url="http://10.10.65.1:8080/api/v1/clusters/sapujagad/hosts/sapujagad-master01.kayangan.com?fields=metrics/cpu&_="+x+""
    username = "sapujagad"
    password = "kayangan"
    response = requests.get(url, auth=(username, password))
    # print(response.status_code)
    return response.json()

# @app.get("/dashboard/metrics/avgcpu")
# def metricsavgcpu():
#     d=str(datetime.datetime.now())
#     p='%Y-%m-%d %H:%M:%S.%f'
#     a = int(time.mktime(time.strptime(d,p)))
#     e = int(time.mktime(time.strptime(d,p))) - 3600
#     z = str(a)
#     x = str(e)
#     url="http://10.10.65.1:8080/api/v1/clusters/sapujagad?fields=metrics/cpu/Nice._avg["+x+","+z+",15],metrics/cpu/System._avg["+x+","+z+",15],metrics/cpu/User._avg["+x+","+z+",15],metrics/cpu/Idle._avg["+x+","+z+",15]&_="+z+""
#     username = "sapujagad"
#     password = "kayangan"
#     response = requests.get(url, auth=(username, password))
#     # print(response.status_code)
#     return response.json()


@app.get("/dashboard/metrics/avgcpu")
def metricsavgcpu():
    d=str(datetime.datetime.now())
    p='%Y-%m-%d %H:%M:%S.%f'
    a = int(time.mktime(time.strptime(d,p)))
    e = int(time.mktime(time.strptime(d,p))) - 3600
    z = str(a)
    x = str(e)
    url="http://10.10.65.1:8080/api/v1/clusters/sapujagad?fields=metrics/cpu/Nice._avg["+x+","+z+",15],metrics/cpu/System._avg["+x+","+z+",15],metrics/cpu/User._avg["+x+","+z+",15],metrics/cpu/Idle._avg["+x+","+z+",15]&_="+z+""
    username = "sapujagad"
    password = "kayangan"
    response = requests.get(url, auth=(username, password))
    test1 = str(response.json())
    test2 = test1.replace("[", "{" )
    test3 = test2.replace("]", "}")
    # test = json.loads(test3)
    test4 = test3.replace("'", '"')  
    # test4 = test3a[:-1]
    # data = json.loads(test4)
    data = json.loads(test4)
    return jsonify(data)
#     return (test4)
    



if __name__ == "__main__":
    app.run(debug=True)
