FROM python:3.11-bullseye@sha256:21ce92a075cf9c454a936f925e058b4d8fc0cfc7a05b9e877bed4687c51a5658
RUN apt update && apt install -y iproute2 vim
WORKDIR /app

EXPOSE 8000

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./source/expenses .