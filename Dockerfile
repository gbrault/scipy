from jupyter/scipy-notebook

COPY ./requirements.txt /home/jovyan
RUN pip install -r /home/jovyan/requirments.txt
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

USER root
RUN usermod -aG sudo $NB_USER
RUN echo "jovyan ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER $NB_UID
ENTRYPOINT ["/tini", "--"]
CMD ["supervisord"]
