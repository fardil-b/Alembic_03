"""create initial schema

Revision ID: cccaca70c0e6
Revises: 
Create Date: 2024-07-09 15:21:58.141201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cccaca70c0e6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Create schema
    op.execute('CREATE SCHEMA IF NOT EXISTS my_schema')

    # Create table within schema
    op.execute('''
    CREATE TABLE my_schema.user (
        id INT PRIMARY KEY,
        name VARCHAR(255) NOT NULL
    )
    ''')


def downgrade() -> None:
    op.execute('''
    DROP TABLE my_schema.user
    ''')
