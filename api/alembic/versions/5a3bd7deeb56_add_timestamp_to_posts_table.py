"""Add timestamp to posts table

Revision ID: 5a3bd7deeb56
Revises: 886696a53236
Create Date: 2024-03-24 19:08:31.338701

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a3bd7deeb56'
down_revision = '886696a53236'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('created_at', sa.DateTime, nullable=False, default=sa.func.now()))
    op.add_column('posts', sa.Column('updated_at', sa.DateTime, nullable=False, default=sa.func.now()))

def downgrade():
    op.drop_column('posts', 'created_at')
    op.drop_column('posts', 'updated_at')
