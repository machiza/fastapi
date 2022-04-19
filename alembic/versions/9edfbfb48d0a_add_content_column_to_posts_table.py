"""add content column to posts table

Revision ID: 9edfbfb48d0a
Revises: 3f797c4b9013
Create Date: 2022-04-19 15:00:43.300667

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9edfbfb48d0a'
down_revision = '3f797c4b9013'
branch_labels = None
depends_on = None


def upgrade():
  op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
  pass


def downgrade():
  op.drop_column('posts', 'content')
  pass
