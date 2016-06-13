FROM alpine
MAINTAINER bdbai <htbai1998m@hotmail.com>

ADD ./requirements.txt /app/requirements.txt
WORKDIR /app

RUN apk --no-cache --update add python3 libjpeg-turbo python3-dev build-base linux-headers libjpeg-turbo-dev zlib-dev \
    && cp /lib/libz.so /usr/lib/libz.so \
    && python3 -m ensurepip --upgrade\
    && pip3 install gunicorn \
    && pip3 install -r requirements.txt \
    && apk del python3-dev build-base linux-headers libjpeg-turbo-dev zlib-dev

ENV DATA_PATH /var/data/blog_project/db.sqlite3
VOLUME ["/var/data/blog_project"]
EXPOSE 4000
CMD ["/bin/sh", "./docker/start.sh"]

ADD . /app

