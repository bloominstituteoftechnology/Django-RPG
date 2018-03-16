FROM python:alpine3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

ADD requirements.txt /code/

RUN apk update && apk add alpine-sdk && apk add postgresql-dev

RUN pip install -r requirements.txt
