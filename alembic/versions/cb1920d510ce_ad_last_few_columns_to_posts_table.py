"""ad last few columns to posts table

Revision ID: cb1920d510ce
Revises: 3fe43c5713cf
Create Date: 2022-04-19 15:59:25.410711

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb1920d510ce'
down_revision = '3fe43c5713cf'
branch_labels = None
depends_on = None


def upgrade():
  op.add_column('posts', sa.Column(
		'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
  op.add_column('posts', sa.Column(
    'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text
    ('NOW()')),)
  pass


def downgrade():
  op.drop_column('posts', 'published')
  op.drop_column('posts', 'created_at')
  pass
