FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD ./src/ /app/src/

WORKDIR /app/src/
RUN pip install -r requirements.txt

