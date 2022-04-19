"""create posts table

Revision ID: 3f797c4b9013
Revises: 
Create Date: 2022-04-19 12:54:07.238657

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f797c4b9013'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
  op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                  primary_key=True), sa.Column('title', sa.String(), nullable=False))
  pass


def downgrade():
  op.drop_table('posts')
  pass
