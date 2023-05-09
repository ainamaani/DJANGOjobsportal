FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /appl

ADD . /appl

COPY ./requirements.txt /appl/requirements.txt

RUN pip install -r requirements.txt

COPY . /appl



