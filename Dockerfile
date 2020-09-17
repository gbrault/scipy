from jupyter/scipy-notebook

COPY ./requirements.txt /home/jovyan/
RUN pip install -r /home/jovyan/requirements.txt

COPY supervisord.conf /home/jovyan/supervisord.conf
COPY monitor.py /home/jovyan/

USER root
RUN apt update -yq
# needed for latex in matplotlib
RUN apt install -yq cm-super
RUN usermod -aG sudo $NB_USER
RUN echo "jovyan ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
USER $NB_UID
# RUN ls /opt/conda/bin/ -al

ENTRYPOINT ["tini", "--"]
CMD ["/opt/conda/bin/supervisord", "-n", "-c", "/home/jovyan/supervisord.conf"]
# CMD [ "start-notebook.sh" ]
