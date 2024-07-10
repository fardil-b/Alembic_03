"""apply schema from file

Revision ID: 11fe6d3b8bc6
Revises: cccaca70c0e6
Create Date: 2024-07-10 16:32:50.435708

"""
from alembic import op
import sqlalchemy as sa
import os


# revision identifiers, used by Alembic.
revision = '11fe6d3b8bc6'
down_revision = 'cccaca70c0e6'
branch_labels = None
depends_on = None


def upgrade():
    schema_path = os.path.join(os.path.dirname(__file__), '..', 'schema.sql')
    with open(schema_path) as f:
        sql_commands = f.read()
    op.execute(sql_commands)


def downgrade():
    op.execute('''
    DROP TABLE my_schema.products;
    DROP TABLE my_schema.user;
    DROP SCHEMA my_schema;
    ''')
