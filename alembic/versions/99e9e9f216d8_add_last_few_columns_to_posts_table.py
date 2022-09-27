"""add last few columns to posts table

Revision ID: 99e9e9f216d8
Revises: 652e25af44aa
Create Date: 2022-09-27 13:50:21.968474

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99e9e9f216d8'
down_revision = '652e25af44aa'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
