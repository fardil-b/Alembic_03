"""single script testing

Revision ID: 577f89fc7fb2
Revises: 13ab7de1ddad
Create Date: 2024-07-11 17:31:24.411317

"""
from alembic import op
import sqlalchemy as sa
import os

# revision identifiers, used by Alembic.
revision = '577f89fc7fb2'
down_revision = '13ab7de1ddad'
branch_labels = None
depends_on = None


def run_sql_script(operation):
    script_path = os.path.join(os.path.dirname(__file__), 'sql', 'combined_alter_existing_schema.sql')
    with open(script_path, 'r') as f:
        sql_commands = f.read()
    
    # Replace the placeholder with the actual operation
    sql_commands = sql_commands.replace('{operation}', operation)
    
    # Log the SQL commands being executed
    print(f"Executing SQL script with operation: {operation}")
    print(sql_commands)
    
    # Execute the entire block as a single command
    try:
        op.execute(sql_commands)
    except Exception as e:
        print(f"Failed to execute SQL script with operation: {operation}")
        print(f"Error: {e}")

def upgrade():
    run_sql_script('upgrade')

def downgrade():
    run_sql_script('downgrade')
