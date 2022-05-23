#!/bin/sh

CURRENT_ENTRYPOINT="${CURRENT_MOUNT_DIR}/deploy/docker/docker-entrypoint.sh"

echo 'Init: Go ...'

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
        --current_mount_dir="${CURRENT_MOUNT_DIR}"
fi

# Build
cd "${CURRENT_MOUNT_DIR}/app"
go build main.go

# Local solution entrypoint
if [ -f "${CURRENT_ENTRYPOINT}" ]; then
    "${CURRENT_ENTRYPOINT}"
fi

# Run
./main

# Alive until a manual stop
sleep infinity
