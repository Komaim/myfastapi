"""add content column to posts table

Revision ID: c3a2bdba6fd7
Revises: 52fa6ebd5c94
Create Date: 2022-09-27 13:16:19.867848

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3a2bdba6fd7'
down_revision = '52fa6ebd5c94'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
