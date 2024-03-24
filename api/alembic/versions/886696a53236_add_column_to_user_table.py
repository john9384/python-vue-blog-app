"""Add column to user table

Revision ID: 886696a53236
Revises: c3911717669c
Create Date: 2024-03-24 19:01:02.778030

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '886696a53236'
down_revision = 'c3911717669c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('is_active', sa.Boolean, nullable=False, default=False))
    op.add_column('users', sa.Column('created_at', sa.DateTime, nullable=False, default=sa.func.now()))
    op.add_column('users', sa.Column('updated_at', sa.DateTime, nullable=False, default=sa.func.now()))

def downgrade():
    op.drop_column('users', 'is_active')
    op.drop_column('users', 'created_at')
    op.drop_column('users', 'updated_at')