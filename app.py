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

class my_dictionary(dict):
    def __init__(self):
        self = dict()

    # Function to add key:value
    def add(self, key, value):
        self[key] = value

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
    # print(response.status_code)
    return response.json()

@app.get("/dashboard/metrics/avgnetwork")
def metricsavgnetwork():
    d=str(datetime.datetime.now())
    p='%Y-%m-%d %H:%M:%S.%f'
    a = int(time.mktime(time.strptime(d,p)))
    e = int(time.mktime(time.strptime(d,p))) - 3600
    z = str(a)
    x = str(e)
    url="http://10.10.65.1:8080/api/v1/clusters/sapujagad/?fields=metrics/network/In._avg["+x+","+z+",15],metrics/network/Out._avg["+x+","+z+",15]&_="+z+""
    username = "sapujagad"
    password = "kayangan"
    response = requests.get(url, auth=(username, password))
    # print(response.status_code)
    return response.json()

@app.get("/dashboard/metrics/clusterload")
def metricsclusterload():
    d=str(datetime.datetime.now())
    p='%Y-%m-%d %H:%M:%S.%f'
    a = int(time.mktime(time.strptime(d,p)))
    e = int(time.mktime(time.strptime(d,p))) - 3600
    z = str(a)
    x = str(e)
    url="http://10.10.65.1:8080/api/v1/clusters/sapujagad/?fields=metrics/load/1-min._avg["+x+","+z+",15],metrics/load/CPUs._avg["+x+","+z+",15],metrics/load/Nodes._avg["+x+","+z+",15],metrics/load/Procs._avg["+x+","+z+",15]&_="+z+""
    username = "sapujagad"
    password = "kayangan"
    response = requests.get(url, auth=(username, password))
    # print(response.status_code)
    return response.json()


@app.get("/dashboard/metrics/avgmemoryusage")
def metricsavgmemoryusage():
    d=str(datetime.datetime.now())
    p='%Y-%m-%d %H:%M:%S.%f'
    a = int(time.mktime(time.strptime(d,p)))
    e = int(time.mktime(time.strptime(d,p))) - 3600
    z = str(a)
    x = str(e)
    url="http://10.10.65.1:8080/api/v1/clusters/sapujagad/?fields=metrics/memory/Buffer._avg["+x+","+z+",15],metrics/memory/Cache._avg["+x+","+z+",15],metrics/memory/Share._avg["+x+","+z+",15],metrics/memory/Swap._avg["+x+","+z+",15],metrics/memory/Total._avg["+x+","+z+",15],metrics/memory/Use._avg["+x+","+z+",15]&_="+z+""
    username = "sapujagad"
    password = "kayangan"
    response = requests.get(url, auth=(username, password))
    # print(response.status_code)
    return response.json()

@app.get("/heatmaps")
def heatmaps():
    url = 'http://10.10.65.1:8080/api/v1/clusters/sapujagad/hosts?fields=metrics/disk/disk_free,metrics/disk/disk_total,metrics/load/load_one&minimal_response=true&page_size=100&from=0'
    username = "sapujagad"
    password = "kayangan"
    response = requests.get(url, auth=(username, password))
    x = response.json()
    a = x['items']
    # [0]['Hosts']['host_name']
    
    n=len(a)
    dict_obj = my_dictionary()   
    for  user in a:
        for i in range(0, n):
            dict_obj.add(i,user['Hosts']['host_name'])
    # udin = list(a)   
    
    # __init__ function

        
    return dict_obj

@app.get("/heatmets/yarn/totalallocatableram")
def totalallocatableram():
    d=str(datetime.datetime.now())
    p='%Y-%m-%d %H:%M:%S.%f'
    a = int(time.mktime(time.strptime(d,p)))
    z = str(a)
    url="http://10.10.65.1:8080/api/v1/clusters/sapujagad/services/YARN/components/NODEMANAGER?fields=host_components/metrics/yarn/AllocatedGB,host_components/metrics/yarn/AvailableGB&format=null_padding&_="+z+""
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
#     test1 = str(response.json())
#     test2 = test1.replace("[", "{" )
#     test3 = test2.replace("]", "}")
#     # test = json.loads(test3)
#     test4 = test3.replace("'", '"')  
#     # test4 = test3a[:-1]
#     # data = json.loads(test4)
# #     data = json.loads(test4)
# #     return jsonify(data)
#     return (test4)
    



if __name__ == "__main__":
    app.run(debug=True)
