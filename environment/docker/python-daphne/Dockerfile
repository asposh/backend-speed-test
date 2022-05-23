FROM asposh/bst-ubuntu-common

# Copy deploy directory
COPY ./deploy /var/deploy

# Install packages
RUN pip3 install -r /var/deploy/python/requirements.txt

EXPOSE 80 443

ENTRYPOINT ["/var/deploy/docker-entrypoint.sh"]
