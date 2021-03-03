web: python server/manage.py collectstatic --noinput; gunicorn --chdir server configuration.asgi:application -b 0.0.0.0:$PORT -k uvicorn.workers.UvicornWorker
