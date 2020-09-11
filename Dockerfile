from jupyter/scipy-notebook

COPY ./requirements.txt /home/jovyan
RUN pip install -r /home/jovyan/requirements.txt
COPY supervisord.conf /home/jovyan/supervisord.conf

USER root
RUN usermod -aG sudo $NB_USER
RUN echo "jovyan ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER $NB_UID
ENTRYPOINT ["/tini", "--"]
CMD ["supervisord -n -c /home/jovyan/supervisord.conf"]
