FROM python:3.7.3-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# install build/runtime dependencies inside the container
RUN apk add --no-cache make build-base libffi-dev openssl postgresql-client postgresql-dev
RUN pip install --no-cache-dir pipenv

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# install language-level dependencies inside the container
COPY Pipfile Pipfile.lock /usr/src/app/
RUN pipenv install --deploy --dev --ignore-pipfile --system

# copy the application source into the container
COPY . /usr/src/app

EXPOSE 8000