# syntax=docker/dockerfile:1

# -----------------------Base Layer-----------------------
FROM python:3 as base

# Work Directory
WORKDIR /app

# Environment Variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y netcat

# Dependencies
RUN pip install --upgrade pip
COPY ./requirements .

# Entrypoint.sh
COPY /docker/django/entrypoint.sh /django_env/entrypoint.sh
RUN sed -i 's/\r$//g' /django_env/entrypoint.sh
RUN chmod +x /django_env/entrypoint.sh

# Start Script
COPY ./docker/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start
# -----------------------Base Layer-----------------------

# --------------------Development Layer-------------------
FROM base as dev

ENV RUN_ENVIRONMENT development

RUN pip install -r local.txt

ENTRYPOINT ["/django_env/entrypoint.sh"]
# --------------------Development Layer-------------------

# --------------------Production Layer--------------------
FROM base as prod

ENV RUN_ENVIRONMENT production

RUN pip install -r production.txt

ENTRYPOINT ["/django_env/entrypoint.sh"]
# --------------------Production Layer--------------------
