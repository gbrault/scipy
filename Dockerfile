from jupyter/scipy-notebook
USER root

RUN usermod -aG sudo $NB_USER
RUN echo "jovyan ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER $NB_UID
