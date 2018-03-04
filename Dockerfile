FROM alpine:3.6


RUN apk add --no-cache \
        uwsgi \
        uwsgi-python3 \
        python3

RUN mkdir -p /deploy/app
COPY . /deploy/app

RUN pip3 install --no-cache-dir -r /deploy/app/requirements.txt

WORKDIR /deploy/app

EXPOSE 3031

ENTRYPOINT [ "uwsgi", "--socket", "0.0.0.0:3031", \
               "--plugins", "python3", \
               "--protocol", "uwsgi", \
               "--wsgi", "app:app" ]
