FROM nginx:alpine
MAINTAINER bdbai <htbai1998m@hotmail.com>

RUN apk --no-cache --update add python3 python3-dev build-base linux-headers libjpeg-turbo-dev zlib-dev \
    && cp /lib/libz.so /usr/lib/libz.so \
    && python3 -m ensurepip \
    && pip3 install uwsgi \
    && mkdir /var/log/uwsgi

ADD . /app
WORKDIR /app

RUN pip3 install -r requirements.txt \
    && chmod +x docker/start.sh \
    && cp docker/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
CMD ["./docker/start.sh"]
