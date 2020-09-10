# Monitoring JoD running notebooks
from notebook import notebookapp
import os
import time
import requests
import datetime

jod_url = os.getenv("JOD_URL", None)
sleep = os.getenv("JOD_SLEEP", None)
servers = list(notebookapp.list_running_servers())
token = servers[0]['token']

if jod_url is not None and sleep is not None and token is not None:
    sleep = int(sleep)
    while True:
        timestamp = datetime.datetime.now().strftime('%s')
        requests.get(jod_url+f"&token={token}&timestamp={timestamp}")
        time.sleep(sleep)