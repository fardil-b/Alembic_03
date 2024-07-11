"""apply changes from scripts

Revision ID: 620394681108
Revises: 11fe6d3b8bc6
Create Date: 2024-07-11 10:55:58.783112

"""
from alembic import op
import sqlalchemy as sa
import os

# revision identifiers, used by Alembic.
revision = '620394681108'
down_revision = '11fe6d3b8bc6'
branch_labels = None
depends_on = None

def upgrade():
    schema_path = os.path.join(os.path.dirname(__file__), 'sql', 'upgrade_schema.sql')
    with open(schema_path) as f:
        sql_commands = f.read()
    op.execute(sql_commands)

def downgrade():
    schema_path = os.path.join(os.path.dirname(__file__), 'sql', 'downgrade_schema.sql')
    with open(schema_path) as f:
        sql_commands = f.read()
    op.execute(sql_commands)