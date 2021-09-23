FROM python:3.8-slim-buster as base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/scripts:${PATH}"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get upgrade


RUN apt-get --no-install-recommends -y install python3.7-dev \
    build-essential \
    curl  \
    jq \
    git \
    nano \
    python-pil \
    libpq-dev \
    gettext

COPY requirements requirements
RUN pip install --upgrade pip
RUN pip install --no-cache -r requirements/development.txt

COPY . /opt/project

RUN chmod +x /opt/project/compose/local/django/entrypoint.sh

ENTRYPOINT ["/opt/project/compose/local/django/entrypoint.sh"]