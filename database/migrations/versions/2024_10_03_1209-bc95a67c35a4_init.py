"""init

Revision ID: bc95a67c35a4
Revises: 
Create Date: 2024-10-03 12:09:14.205797

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bc95a67c35a4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('breeds',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('breeds_pkey'))
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=False),
    sa.Column('refresh_token', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text("timezone('utc', now())"), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text("timezone('utc', now())"), nullable=False),
    sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('user_pkey')),
    sa.UniqueConstraint('username', name=op.f('user_username_key'))
    )
    op.create_index(op.f('ix_user_deleted_at'), 'user', ['deleted_at'], unique=False)
    op.create_table('kittens',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('color', sa.String(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('breed_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text("timezone('utc', now())"), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text("timezone('utc', now())"), nullable=False),
    sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['breed_id'], ['breeds.id'], name=op.f('kittens_breed_id_fkey'), onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('kittens_pkey'))
    )
    op.create_index(op.f('ix_kittens_deleted_at'), 'kittens', ['deleted_at'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_kittens_deleted_at'), table_name='kittens')
    op.drop_table('kittens')
    op.drop_index(op.f('ix_user_deleted_at'), table_name='user')
    op.drop_table('user')
    op.drop_table('breeds')
    # ### end Alembic commands ###
