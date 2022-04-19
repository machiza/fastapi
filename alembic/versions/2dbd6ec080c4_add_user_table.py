"""add user table

Revision ID: 2dbd6ec080c4
Revises: 9edfbfb48d0a
Create Date: 2022-04-19 15:25:43.826747

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2dbd6ec080c4'
down_revision = '9edfbfb48d0a'
branch_labels = None
depends_on = None


def upgrade():
  op.create_table('users',
                  sa.Column('id', sa.Integer(), nullable=False),
                  sa.Column('email', sa.String(), nullable=False),
                  sa.Column('password', sa.String(), nullable=False),
                  sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                            server_default=sa.text('now()'), nullable=False),
                  sa.PrimaryKeyConstraint('id'),
                  sa.UniqueConstraint('email'),
                  )
  pass


def downgrade():
  op.drop_table('users')
  pass
