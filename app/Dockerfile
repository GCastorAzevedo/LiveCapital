FROM python:3.6

MAINTAINER Gabriel Castor

ADD . /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD exec gunicorn app.swgi:application \
    --env DJANGO_SETTINGS_MODULE=app.settings \
    --bind 0.0.0.0:8000 \
    --workers 9

# Get pip to download and install requirements:
#RUN pip install --no-cache-dir -r requirements.txt
# Expose ports
#EXPOSE 8000
# default command to execute    
#CMD exec gunicorn djangoapp.wsgi:application --bind 0.0.0.0:8000 --workers 3