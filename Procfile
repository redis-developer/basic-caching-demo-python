web: python server/manage.py collectstatic --noinput; gunicorn --chdir server configuration.asgi:application -b 127.0.0.1:$PORT -k uvicorn.workers.UvicornWorker
