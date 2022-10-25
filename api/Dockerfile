# The API gateway will only provide a data access point and will be
# kept as light weight as possible to ease scalability.
# Everything can be run within a minimal apline image running python >= 3.10
FROM python:3.11-alpine

RUN apk update
RUN pip install --no-cache-dir pipenv

WORKDIR /app
COPY Pipfile Pipfile.lock entrypoint.sh ./
COPY src ./src

RUN pipenv install --system --deploy

EXPOSE 5000
ENTRYPOINT ["/app/entrypoint.sh"]