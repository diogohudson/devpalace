FROM python:3.11-slim-buster

ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends build-essential 
RUN apt-get install -y curl gdal-bin libpq-dev postgresql-client 
RUN rm -rf /var/lib/apt/lists/* 

COPY ./requirements/ /requirements

RUN pip install --upgrade pip && pip install -r /requirements/dev.txt

# create directory for the app user
RUN mkdir -p devpalace

COPY ./devpalace devpalace

WORKDIR devpalace

