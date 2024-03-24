"""Add post table

Revision ID: c3911717669c
Revises: 180e2db526eb
Create Date: 2024-03-24 18:47:39.600795

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, String

# revision identifiers, used by Alembic.
revision = 'c3911717669c'
down_revision = '180e2db526eb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'posts',
        Column('id', String(150), primary_key=True, unique=True),
        Column('creator_id', String(150), nullable=False),
        Column('title', String(100), nullable=False),
        Column('content', String(500), nullable=False),
        Column('image', String(500), nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table('posts')
