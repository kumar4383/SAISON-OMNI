FROM python:3.10-alpine

# PYTHONUNBUFFERED variable is used for non-buffered stdout
ENV PYTHONUNBUFFERED=1

# changing our working directory to be /search
WORKDIR /saison_omni

RUN apk add librdkafka-dev build-base
RUN apk update && apk add libpq-dev gcc

RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy --ignore-pipfile

# copying the whole django application
COPY . ./

# exposing our django port: 8080
EXPOSE 8080

CMD ["/bin/sh", "/saison_omni/runserver.sh"]
