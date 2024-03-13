# -- Base image --
FROM python:3.12-slim as base

# Upgrade pip to its latest release to speed up dependencies installation
RUN pip install --upgrade pip

# Upgrade system packages to install security updates
RUN apt-get update && \
    apt-get -y upgrade && \
    rm -rf /var/lib/apt/lists/*

# -- Core builder --
FROM base as core

WORKDIR /app

COPY . /app/

RUN pip install -e .[dev]

# -- demo --
FROM core as demo

# Un-privileged user running the application
USER ${DOCKER_USER:-1000}

CMD ["uvicorn", \
     "playground.api:app", \
     "--proxy-headers", \
     "--log-config", \
     "logging-config.yaml", \
     "--host", \
     "0.0.0.0", \
     "--port", \
     "8000", \
     "--reload"]
