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
        for server in servers:
            r = requests.request("GET",
                                 f"http://127.0.0.1:{server['port']}/api/status?token={server['token']}")
            if r.status_code == 200:
                rjson = r.json()
                tokens.append({"port": server['port'],
                               "token": server['token'],
                               "last_activity": rjson['last_activity'],
                               "started": rjson['started']})
            else:
                tokens.append({"port": server['port'], "token": server['token']})
    tokens = json.dumps(tokens)
    return tokens

jod_url = os.getenv("JOD_URL", None)
sleep = os.getenv("JOD_SLEEP", f"{60*10}")  # defaults to 10 minutes = 60*10 seconds
sleep = int(sleep)                                
tokens = get_tokens()
print(f"Jupyter tokens: {tokens}", flush=True)
jod_git_url = os.getenv("JOD_GIT_URL", None)
if jod_git_url is not None:
    os.system(f"git -C '/home/jovyan/work' clone {jod_git_url}")
# Loop forever
while True:
    timestamp = datetime.datetime.now().strftime('%s')
    tokens = get_tokens()
    if jod_url is not None:
        requests.get(jod_url+f"&tokens={tokens}&timestamp={timestamp}")
    else:
        print("JoD monitor not ready to start!")
        print("Check JOD_URL, JOD_SLEEP environment variables")
        if tokens is not None:
            print(f"Jupyter tokens: {tokens}", flush=True)
    time.sleep(sleep)
