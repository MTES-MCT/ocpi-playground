# -- Base image --
FROM python:3.12-slim as base

ARG DOCKER_USER=1000

# Upgrade pip to its latest release to speed up dependencies installation
RUN pip install --upgrade pip

# Upgrade system packages to install security updates
RUN apt-get update && \
    apt-get -y upgrade && \
    rm -rf /var/lib/apt/lists/*

# Create docker user home directory
ENV HOME=/home/ocpi
ENV VENV_PATH=${HOME}/venv
ENV PATH=${VENV_PATH}/bin:${PATH}
RUN mkdir ${HOME} && \
      chown ${DOCKER_USER} ${HOME}

# Un-privileged user building the application
USER ${DOCKER_USER:-1000}
RUN python3 -m venv ${VENV_PATH} && \
      ${VENV_PATH}/bin/pip install poetry

# Back to root
USER root:root

# -- Core builder --
FROM base as core

RUN mkdir /app && \
      chown ${DOCKER_USER} /app
WORKDIR /app

COPY --chown=${DOCKER_USER} . /app/

# Un-privileged user building the application
USER ${DOCKER_USER}
RUN poetry install --with dev

# Back to root
USER root:root

# -- demo --
FROM core as demo

# Un-privileged user running the application
USER ${DOCKER_USER:-1000}

CMD ["poetry", \
     "run", \
     "uvicorn", \
     "playground.api:app", \
     "--proxy-headers", \
     "--log-config", \
     "logging-config.yaml", \
     "--host", \
     "0.0.0.0", \
     "--port", \
     "8000", \
     "--reload"]
