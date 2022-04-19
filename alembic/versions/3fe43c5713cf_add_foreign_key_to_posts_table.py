"""add foreign-key to posts table

Revision ID: 3fe43c5713cf
Revises: 2dbd6ec080c4
Create Date: 2022-04-19 15:33:28.449693

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fe43c5713cf'
down_revision = '2dbd6ec080c4'
branch_labels = None
depends_on = None


def upgrade():
  op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
  op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users",
	local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
  pass


def downgrade():
  op.drop_constraint('post_users_fk', table_name="posts")
  op.drop_column('posts', 'owner_id')
  pass
