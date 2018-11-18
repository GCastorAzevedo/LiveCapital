#!/bin/bash

#Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn app.wsgi:application \
    --env DJANGO_SETTINGS_MODULE=app.settings \
    --bind 0.0.0.0:8000 \
    --workers 9