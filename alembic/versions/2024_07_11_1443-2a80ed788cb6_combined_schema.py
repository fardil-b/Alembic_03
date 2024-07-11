"""combined_schema

Revision ID: 2a80ed788cb6
Revises: 620394681108
Create Date: 2024-07-11 14:43:48.950648

"""
from alembic import op
import sqlalchemy as sa
import os

# revision identifiers, used by Alembic.
revision = '2a80ed788cb6'
down_revision = '620394681108'
branch_labels = None
depends_on = None


def run_sql_script(operation):
    script_path = os.path.join(os.path.dirname(__file__), 'sql', 'combined_schema.sql')
    with open(script_path) as f:
        sql_commands = f.read()
    sql_commands = sql_commands.replace("operation := 'upgrade';", f"operation := '{operation}';")
    op.execute(sql_commands)

def upgrade():
    run_sql_script('upgrade')

def downgrade():
    run_sql_script('downgrade')