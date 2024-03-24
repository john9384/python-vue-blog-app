"""Add user table

Revision ID: 180e2db526eb
Revises: 
Create Date: 2024-03-24 18:47:30.563957

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, String


# revision identifiers, used by Alembic.
revision = '180e2db526eb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        Column('id', String(150), primary_key=True, unique=True),
        Column('firstname', String(50), nullable=False),
        Column('lastname', String(50), nullable=False),
        Column('email', String(120), unique=True, nullable=False),
        Column('username', String(80), unique=True, nullable=False),
        Column('password', String(1000), nullable=False),       
    )


def downgrade() -> None:
    op.drop_table('users')
