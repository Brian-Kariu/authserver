# syntax = docker/dockerfile:1.2
FROM python:3.10

RUN apt-get update;

ENV PYTHONUNBUFFERED 1
WORKDIR /app

RUN --mount=type=secret,id=_env,dst=/etc/secrets/.env cp /etc/secrets/.env /app/.env
COPY . /app/

RUN chmod +x *.sh
RUN pip install --upgrade pip
RUN pip install .[dev] 

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]

