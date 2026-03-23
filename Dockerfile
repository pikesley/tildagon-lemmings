FROM python:3.13

ARG APP

WORKDIR /opt/${APP}
RUN apt-get update -y && \
    apt-get install -y make build-essential zlib1g-dev libjpeg-dev

COPY ./requirements.txt ${WORKDIR}

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

COPY ./ ${WORKDIR}
