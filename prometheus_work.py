import prometheus_client
from fastapi import FastAPI
import time
import requests
app=FastAPI()

@app.get("/hello")
async def sa():


    prome_sql = 'sum(rate(container_cpu_usage_seconds_total{container_name!="POD",namespace!="kube-system"}[5m])) by (namespace)'

    response = requests.get('http://168.119.224.222:31338/api/v1/query',
                            params={'query': prome_sql})
    print(response.json()["data"]['result'])
    return response.json()["data"]['result']

@app.get("/cpu-usage")
async def kubernetes_cpu_usage():
    prome_sql = 'sum(rate(container_cpu_usage_seconds_total{container_name!="POD",pod_name!="*"}[30m]))'
    response = requests.get('http://168.119.224.222:31338/api/v1/query',
                            params={'query': prome_sql})
    return response.json()["data"]['result']

#TRUE
@app.get("/mem-usage")
async def kubernetes_total_memory_usage():
    prome_sql = 'sum(container_memory_usage_bytes{container_name!="POD",container_name=""})'
    response = requests.get('http://168.119.224.222:31338/api/v1/query',
                            params={'query': prome_sql})
    return response.json()["data"]['result']

@app.get("/node-usage")
async def kubernetes_total_memory_usage():
    prome_sql = '(container_memory_usage_bytes{container="POD"})'
    response = requests.get('http://168.119.224.222:31338/api/v1/query',
                            params={'query': prome_sql})
    return response.json()["data"]['result']

#TRUE
@app.get("/kubernetes-cpu-total")
async def kubernetes_total_cpu_usage():
    prome_sql = '(sum(container_cpu_usage_seconds_total))'
    response = requests.get('http://168.119.224.222:31338/api/v1/query',
                            params={'query': prome_sql})
    return response.json()["data"]['result']

#TRUE
@app.get("/kubernetes-cpu-total/container")
async def kubernetes_container_cpu_usage():
    prome_sql = 'sum(container_cpu_usage_seconds_total{container=""})'
    response = requests.get('http://168.119.224.222:31338/api/v1/query',
                            params={'query': prome_sql})
    return response.json()["data"]['result']

#TRUE
@app.get("/kubernetes-cpu-total/pod")
async def kubernetes_pod_cpu_usage():
    prome_sql = 'sum(container_cpu_usage_seconds_total{pod=""})'
    response = requests.get('http://168.119.224.222:31338/api/v1/query',
                            params={'query': prome_sql})
    return response.json()["data"]['result']

#TRUE
@app.get("/kubernetes-cpu-total/namespace")
async def kubernetes_namespace_cpu_usage():
    prome_sql = 'sum(container_cpu_usage_seconds_total{namespace=""})'
    response = requests.get('http://168.119.224.222:31338/api/v1/query',
                            params={'query': prome_sql})
    return response.json()["data"]['result']


@app.get("/kubernetes-memory-total")
async def kubernetes_namespace_cpu_usage():
    prome_sql = 'sum(container_memory_usage_bytes)'
    response = requests.get('http://168.119.224.222:31338/api/v1/query',
                            params={'query': prome_sql})
    return response.json()["data"]['result']

@app.get("/kubernetes-memory-total/node")
async def kubernetes_namespace_cpu_usage():
    prome_sql = 'sum(container_memory_usage_bytes{node=""})'
    response = requests.get('http://168.119.224.222:31338/api/v1/query',
                            params={'query': prome_sql})
    return response.json()["data"]['result']

@app.get("/kubernetes-memory-total/container")
async def kubernetes_namespace_cpu_usage():
    prome_sql = 'sum(container_cpu_usage_seconds_total{container=""})'
    response = requests.get('http://168.119.224.222:31338/api/v1/query',
                            params={'query': prome_sql})
    return response.json()["data"]['result']

@app.get("/kubernetes-memory-total/pod")
async def kubernetes_namespace_cpu_usage():
    prome_sql = 'sum(container_cpu_usage_seconds_total{pod=""})'
    response = requests.get('http://168.119.224.222:31338/api/v1/query',
                            params={'query': prome_sql})
    return response.json()["data"]['result']

@app.get("/kubernetes-memory-total/namespace")
async def kubernetes_namespace_cpu_usage():
    prome_sql = 'sum(container_cpu_usage_seconds_total{namespace=""})'
    response = requests.get('http://168.119.224.222:31338/api/v1/query',
                            params={'query': prome_sql})
    return response.json()
