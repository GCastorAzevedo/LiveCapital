FROM python:3.6

ADD . /usr/src

WORKDIR /usr/src

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

#RUN python manage.py collectstatic

EXPOSE 8000

CMD exec gunicorn app.wsgi:application \
    --env DJANGO_SETTINGS_MODULE=app.settings \
    --bind 0.0.0.0:8000 \
    --workers 9