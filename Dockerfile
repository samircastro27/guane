# pull official base image
ARG BASE_IMAGE=python
ARG IMAGE_TAG=3.9.0-slim-buster

FROM ${BASE_IMAGE}:${IMAGE_TAG} AS requirements-image

# set working directory
WORKDIR /usr/src/app

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get -y update \
    && apt-get upgrade -y \
    && apt-get install -y \
    build-essential \
    ca-certificates \
    curl \
    git \
    gcc \
    python3-dev \
    && apt-get -y clean

# install python dependencies
RUN pip install pipenv==v2021.5.29 --no-cache-dir
COPY Pipfile* ./
RUN pipenv lock -r > requirements.txt

# add app
FROM ${BASE_IMAGE}:${IMAGE_TAG} AS compile-image
WORKDIR /usr/src/app
COPY --from=requirements-image /usr/src/app/requirements.txt /usr/src/app/requirements.txt

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get -y update \
    && apt-get install --no-install-recommends -y \
    curl \
    gcc \
    build-essential \
    python3-dev \
    && apt-get clean \
    && curl -O https://bootstrap.pypa.io/get-pip.py \
    && python get-pip.py \
    && python -m venv /home/venv

ENV PATH="/home/venv/bin:$PATH"
RUN pip install --no-cache-dir -r requirements.txt

FROM ${BASE_IMAGE}:${IMAGE_TAG} AS runtime-image
ARG DEBUG=False
ARG DATABASE_SERVICE=http://kyrk-database.kyrk.svc.cluster.local/
ARG RESULTS_SERVICE=http://kyrk-results-db.kyrk.svc.cluster.local/
ARG LEGACY_SERVICE=http://kyrk-engine.kyrk.svc.cluster.local/
ENV PYTHONUNBUFFERED TRUE
COPY --from=compile-image /home/venv /home/venv
ENV PATH="/home/venv/bin:$PATH"
WORKDIR /usr/src/app
EXPOSE 80
COPY . .
ENTRYPOINT [ "uvicorn", "app.main:app", "--log-level","info","--workers", "1"]