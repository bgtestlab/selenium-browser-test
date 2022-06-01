FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apk add --update --no-cache python3-dev libffi-dev libc-dev gcc linux-headers jq bash curl

COPY ./docker/requirements.txt ./requirements.txt
RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

COPY . ./app
WORKDIR /app/docker
RUN chmod +x wait-for-grid.sh
RUN chmod +x pytest.sh

WORKDIR /app
