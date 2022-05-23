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
}

dp = deploy_tool.DeployTool({'options_available': options_available})

# DB initialization
dp.init_db()

# Build settings.py
dp.build_config(
    '{{current_mount_dir}}/deploy/template.settings.py',
    '{{current_mount_dir}}/app/project/settings.py'
)
