FROM python:3

ENV PYTHONDONTWRITEBYCODE=1
ENV PYTHONUNDUFFERED=1

WORKDIR /app

COPY requirements/* /app/
RUN pip install -r base.txt

COPY . /app/