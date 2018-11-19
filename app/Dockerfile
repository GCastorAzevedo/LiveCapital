FROM python:3.6
#FROM alpine:3.8
#
#RUN apk update && \
#    apk add nginx && \
#    apk add --no-cache python3 && \
#    python3 -m ensurepip && \
#    rm -r /usr/lib/python*/ensurepip && \
#    pip3 install --upgrade pip setuptools && \
#    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
#    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
#    rm -r /root/.cache

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