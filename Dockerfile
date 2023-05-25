FROM python:3.10

RUN mkdir /okpd_app

WORKDIR /okpd_app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
