web: python server/manage.py collectstatic --noinput; gunicorn --chdir server configuration.asgi:application -b 127.0.0.1:5000 -k uvicorn.workers.UvicornWorker
