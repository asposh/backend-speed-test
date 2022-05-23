FROM asposh/bst-ubuntu-common

# Copy deploy directory
COPY ./deploy /var/deploy

# Install packages
RUN apt update \
    && apt install -y \
        golang

EXPOSE 80 443

ENTRYPOINT ["/var/deploy/docker-entrypoint.sh"]
