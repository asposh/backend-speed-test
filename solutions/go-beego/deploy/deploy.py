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
}

dp = deploy_tool.DeployTool({'options_available': options_available})

# Build config
dp.build_config(
    '{{current_mount_dir}}/deploy/template.app.conf',
    '{{current_mount_dir}}/app/conf/app.conf'
)

# DB initialization
dp.init_db()

# Test DB initialization
dp.options['db_name'] += '_test'
dp.init_db()
dp.query_from_file('{{current_mount_dir}}/deploy/dump.sql')
