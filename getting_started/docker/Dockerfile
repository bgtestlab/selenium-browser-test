FROM python:3.9-alpine

COPY requirements.txt /app/requirements.txt
COPY wait-for-grid.sh /app/wait-for-grid.sh
COPY test_headless_chrome.py /app/test_headless_chrome.py

WORKDIR /app

RUN apk add --update --no-cache python3-dev libffi-dev libc-dev gcc linux-headers jq bash curl
RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt
RUN chmod +x wait-for-grid.sh

ENTRYPOINT ["/bin/sh", "wait-for-grid.sh"]
CMD pytest test_headless_chrome.py
