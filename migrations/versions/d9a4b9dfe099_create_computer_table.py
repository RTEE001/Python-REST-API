"""create computer table

Revision ID: d9a4b9dfe099
Revises: 
Create Date: 2022-08-07 17:22:52.910719

"""
from alembic import op
import sqlalchemy as sa

from computer import Computer


# revision identifiers, used by Alembic.
revision = 'd9a4b9dfe099'
down_revision = None


def upgrade():
    
    bind = op.get_bind()
    Computer.__table__.create(bind)


def downgrade():

    op.drop_table('computer')