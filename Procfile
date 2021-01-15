release: python3 manage.py collectstatic
web: gunicorn configuration.asgi:application -b 0.0.0.0:$PORT -k uvicorn.workers.UvicornWorker