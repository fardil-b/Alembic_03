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


def run_sql_script(script_name):
    script_path = os.path.join(os.path.dirname(__file__), 'sql', script_name)
    with open(script_path, 'r') as f:
        sql_commands = f.read()
    
    # Log the SQL commands being executed
    print(f"Executing SQL script: {script_name}")
    print(sql_commands)
    
    # Execute the entire block as a single command
    try:
        op.execute(sql_commands)
    except Exception as e:
        print(f"Failed to execute SQL script: {script_name}")
        print(f"Error: {e}")

def upgrade():
    run_sql_script('upgrade_schema2.sql')

def downgrade():
    run_sql_script('downgrade_schema2.sql')