"""create post table

Revision ID: 52fa6ebd5c94
Revises: 
Create Date: 2022-09-27 12:50:15.089258

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52fa6ebd5c94'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
