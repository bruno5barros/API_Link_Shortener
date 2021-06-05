# The image selected to build our environment
FROM python:3.7-alpine
MAINTAINER BB

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

# Create an app folder run developed code
RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

# Create user to avoid to use root user
RUN adduser -D user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web

# Use the created user
USER user
