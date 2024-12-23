FROM python:3.13.0-alpine3.20 AS base

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /var/app

RUN python3 -m pip install django psycopg[binary]==3.2.3

COPY ./docker/entrypoint.sh /usr/bin/django-entrypoint.sh

ENTRYPOINT ["/usr/bin/django-entrypoint.sh"]
