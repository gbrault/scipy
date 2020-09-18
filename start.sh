sudo su <<HERE
echo "JOD_URL=$JOD_URL" > /home/jovyan/.env
echo "JOD_SLEEP=$JOD_SLEEP" >> /home/jovyan/.env
echo "JOD_GIT_URL=$JOD_GIT_URL" >> /home/jovyan/.env
echo "JOD_AK=$JOD_AK" >> /home/jovyan/.env
chown jovyan:users /home/jovyan/.env
HERE
cd /home/jovyan
/opt/conda/bin/python /home/jovyan/monitor.py
