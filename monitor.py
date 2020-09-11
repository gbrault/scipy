# Monitoring and metering JoD running notebooks
from notebook import notebookapp
import os
import time
import requests
import datetime
import json

def get_tokens():
    tokens = []
    servers = list(notebookapp.list_running_servers())
    if servers is not None and len(servers)>0:
        tokens = [{"port": server['port'], "token": server['token']} for server in servers]
    tokens = json.dumps(tokens)
    return tokens

jod_url = os.getenv("JOD_URL", None)
sleep = os.getenv("JOD_SLEEP", f"{60*1000}")  # defaults to 60 seconds
sleep = int(sleep)
tokens = get_tokens()
print(f"Jupyter tokens: {tokens}")

# Loop forever
while True:
    timestamp = datetime.datetime.now().strftime('%s')
    tokens = get_tokens()
    if jod_url is not None:
        requests.get(jod_url+f"&token={token}&timestamp={timestamp}")
    else:
        print("JoD monitor not ready to start!")
        print("Check JOD_URL, JOD_SLEEP environment variables")
        if tokens is not None:
            print(f"Jupyter tokens: {tokens}")
    time.sleep(sleep)
