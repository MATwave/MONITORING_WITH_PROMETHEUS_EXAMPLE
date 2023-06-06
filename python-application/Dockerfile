
FROM python:3.10.5-alpine3.16 as prod

RUN mkdir /app/
WORKDIR /app/

COPY pyproject.toml poetry.lock /app/
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-ansi

COPY ./src/ /app/

ENV FLASK_APP=server.py
CMD flask run -h 0.0.0 -p 5000
