# Use an official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.9

WORKDIR /usr/src/app/

RUN pwd

# Install dependencies.
COPY requirements.txt .
RUN pip install -r google-cloud-run/requirements.txt

# Copy local code to the container image.
COPY . .

RUN echo "$PWD"
# Service must listen to $PORT environment variable.
# This default value facilitates local development.
ARG REDIS_URL_ADDRESS
ARG SERVICE_URL

ENV ALLOWED_HOSTS=$SERVICE_URL
ENV REDIS_URL=$REDIS_URL_ADDRESS
RUN echo "$REDIS_URL"
ENV PORT 8080
ENV DJANGO_DEBUG True

# Setting this ensures print statements and log messages
# promptly appear in Cloud Logging.
ENV PYTHONUNBUFFERED TRUE

RUN python3 manage.py collectstatic

CMD exec gunicorn configuration.asgi:application -b 0.0.0.0:$PORT -k uvicorn.workers.UvicornWorker