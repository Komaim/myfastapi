"""create posts table

Revision ID: e8afc1395d18
Revises: c3a2bdba6fd7
Create Date: 2022-09-27 13:28:58.911580

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8afc1395d18'
down_revision = 'c3a2bdba6fd7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
