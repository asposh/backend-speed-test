#!/bin/sh

# DB migrate
cd "${CURRENT_MOUNT_DIR}/app"
php bin/console doctrine:migrations:migrate

# Clear cache for test environment
php bin/console cache:clear --env=test
