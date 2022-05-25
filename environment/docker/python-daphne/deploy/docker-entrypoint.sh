#!/bin/sh

CURRENT_ENTRYPOINT="${CURRENT_MOUNT_DIR}/deploy/docker/docker-entrypoint.sh"

echo 'Init...'

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
        --config_nginx="${CONFIG_NGINX}"
fi

# DB migrate
cd "${CURRENT_MOUNT_DIR}/app"
python3 manage.py migrate

# Local solution entrypoint
if [ -f "${CURRENT_ENTRYPOINT}" ]; then
    chmod +x "${CURRENT_ENTRYPOINT}"
    "${CURRENT_ENTRYPOINT}"
fi

# Start Daphne
daphne -e ssl:443:privateKey="${BST_MOUNT_DIR}"/environment/ssl/localhost.key:certKey="${BST_MOUNT_DIR}"/environment/ssl/localhost.crt project.asgi:application

# Alive until a manual stop
sleep infinity
