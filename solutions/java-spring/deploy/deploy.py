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

# DB initialization
dp.init_db()

# Build application.yml
dp.build_config(
    '{{current_mount_dir}}/deploy/template.application.yml',
    '{{current_mount_dir}}/app/src/main/resources/application.yml',
)

# Build build.gradle
dp.build_config(
    '{{current_mount_dir}}/deploy/template.build.gradle',
    '{{current_mount_dir}}/app/build.gradle',
)

# Test DB initialization
dp.options['db_name'] += '_test'
dp.init_db()

# Build application.yml test
dp.build_config(
    '{{current_mount_dir}}/deploy/template.test.application.yml',
    '{{current_mount_dir}}/app/src/test/resources/application.yml',
)
