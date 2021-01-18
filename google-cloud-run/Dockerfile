# Use an official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.9

ENV APP_HOME redis-caching-python
WORKDIR $APP_HOME

RUN pwd
RUN echo "$PWD"
# Install dependencies.
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy local code to the container image.
COPY . .

# Service must listen to $PORT environment variable.
# This default value facilitates local development.
ENV PORT 8080
ENV DJANGO_DEBUG True

# Setting this ensures print statements and log messages
# promptly appear in Cloud Logging.
ENV PYTHONUNBUFFERED TRUE

RUN python3 manage.py collectstatic

CMD exec gunicorn configuration.asgi:application -b 0.0.0.0:$PORT -k uvicorn.workers.UvicornWorker