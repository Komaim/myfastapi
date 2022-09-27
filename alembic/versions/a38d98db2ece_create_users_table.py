"""create users table

Revision ID: a38d98db2ece
Revises: 651629022d86
Create Date: 2022-09-27 13:33:55.402165

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a38d98db2ece'
down_revision = '651629022d86'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users', sa.Column('id', sa.Integer(), nullable=False), sa.Column('email', sa.String(), nullable=False), sa.Column('password', sa.String(), nullable=False), sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False), sa.PrimaryKeyConstraint('id'), sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
