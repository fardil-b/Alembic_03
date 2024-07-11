"""alter_exixting_schema

Revision ID: 13ab7de1ddad
Revises: 2a80ed788cb6
Create Date: 2024-07-11 14:57:35.770216

"""
from alembic import op
import sqlalchemy as sa
import os


# revision identifiers, used by Alembic.
revision = '13ab7de1ddad'
down_revision = '2a80ed788cb6'
branch_labels = None
depends_on = None


def run_sql_script(operation):
    script_path = os.path.join(os.path.dirname(
        __file__), 'sql', 'combined_alter_existing_schema.sql')
    with open(script_path) as f:
        sql_commands = f.read()
    sql_commands = sql_commands.replace(
        "operation := 'upgrade';", f"operation := '{operation}';")
    op.execute(sql_commands)


def upgrade():
    run_sql_script('upgrade')


def downgrade():
    run_sql_script('downgrade')
