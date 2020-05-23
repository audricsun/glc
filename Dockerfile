FROM python:slim

WORKDIR /services/mycli

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv && \
    pipenv install --system

COPY . .



