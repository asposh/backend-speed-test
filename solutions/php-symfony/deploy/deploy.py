# Import deploy_tool
from deploy_tool import deploy_tool


# CLI params initialisation
options_available = {
    'db_type',
    'db_name',
    'db_host',
    'db_port',
    'db_user',
    'db_password',
    'bst_mount_dir',
    'current_mount_dir',
    'config_nginx',
    'config_php',
}

dp = deploy_tool.DeployTool({'options_available': options_available})

# DB initialization
dp.init_db()

# Build Nginx configs
dp.build_config(
    '{{bst_mount_dir}}/environment/nginx/nginx.conf',
    '{{config_nginx}}/nginx.conf'
)
dp.build_config(
    '{{bst_mount_dir}}/environment/nginx/php-symfony/default',
    '{{config_nginx}}/sites-enabled/default'
)

# Build PHP config
dp.build_config(
    '{{bst_mount_dir}}/environment/php/8.1/php.ini',
    '{{config_php}}'
)

# Build .env
dp.build_config(
    '{{current_mount_dir}}/deploy/template.env',
    '{{current_mount_dir}}/app/.env'
)

# Test DB initialization
dp.options['db_name'] += '_test'
dp.init_db()
dp.query_from_file('{{current_mount_dir}}/deploy/dump.sql')
