FROM asposh/bst-ubuntu-common

# Copy deploy directory
COPY ./deploy /var/deploy

# Update Ubuntu packages 
RUN apt update \
    && add-apt-repository ppa:ondrej/nginx \
    && add-apt-repository ppa:ondrej/php

# Install packages
RUN apt update \
    && apt install -y \
        nginx \
        php8.1-fpm \
        php8.1-pgsql \
        php8.1-xml \
        php8.1-mbstring \

    # Composer
    && curl -sS https://getcomposer.org/installer > /tmp/composer.setup \
    && php /tmp/composer.setup --install-dir=/usr/bin --filename=composer \
    && rm /tmp/composer.setup

# Forward access and error logs to stdin/stderr
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log

EXPOSE 80 443

ENTRYPOINT ["/var/deploy/docker-entrypoint.sh"]
