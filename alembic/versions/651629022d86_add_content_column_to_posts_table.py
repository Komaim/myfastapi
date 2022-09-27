"""add content column to posts table

Revision ID: 651629022d86
Revises: e8afc1395d18
Create Date: 2022-09-27 13:30:49.775693

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '651629022d86'
down_revision = 'e8afc1395d18'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass