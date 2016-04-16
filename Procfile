web: gunicorn config.wsgi:application
worker: celery worker --app=oscar.taskapp --loglevel=info
