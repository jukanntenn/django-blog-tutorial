#!/bin/sh

python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput
python3 manage.py collectstatic --noinput > /dev/null

gunicorn -b 0.0.0.0:4000 blog_project.wsgi:application
