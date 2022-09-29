FROM fedora-minimal:latest

RUN microdnf -y update
RUN microdnf -y install python pipenv cronie cronie-anacron

WORKDIR /app
COPY scripts/get-image-data-cron /etc/cron.d/get-image-data-cron
COPY Pipfile Pipfile.lock ./
COPY src ./src

RUN pipenv install --system --deploy

RUN chmod 0644 /etc/cron.d/get-image-data-cron
RUN crontab /etc/cron.d/get-image-data-cron
RUN touch /var/log/cron.log

CMD crond && tail -f /var/log/cron.log