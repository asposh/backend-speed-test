#!/bin/sh

CURRENT_ENTRYPOINT="${CURRENT_MOUNT_DIR}/deploy/docker/docker-entrypoint.sh"

echo 'Init: Nginx, PHP...'

# Php
/etc/init.d/php8.1-fpm start

# Init
if [ -f "${CURRENT_MOUNT_DIR}/deploy/deploy.py" ]; then
    cd "${CURRENT_MOUNT_DIR}/deploy"
    /bin/python3 deploy.py \
        --db_type="${DB_TYPE}" \
        --db_name="${DB_NAME}" \
        --db_host="${DB_HOST}" \
        --db_port="${DB_PORT}" \
        --db_user="${DB_USER}" \
        --db_password="${DB_PASSWORD}" \
        --bst_mount_dir="${BST_MOUNT_DIR}" \
        --current_mount_dir="${CURRENT_MOUNT_DIR}" \
        --config_nginx="${CONFIG_NGINX}" \
        --config_php="${CONFIG_PHP}"

    # Php restart
    /etc/init.d/php8.1-fpm restart
fi

if [ -f "${CURRENT_MOUNT_DIR}/app/composer.json" ]; then
    cd "${CURRENT_MOUNT_DIR}/app"
    composer install
fi

# Local solution entrypoint
if [ -f "${CURRENT_ENTRYPOINT}" ]; then
    chmod +x "${CURRENT_ENTRYPOINT}"
    "${CURRENT_ENTRYPOINT}"
fi

# Nginx
nginx -g 'daemon off;'

# Alive until a manual stop
sleep infinity
