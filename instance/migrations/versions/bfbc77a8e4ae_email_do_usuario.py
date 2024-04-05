"""Email do usuario

Revision ID: bfbc77a8e4ae
Revises: 18237ea40f3f
Create Date: 2024-04-04 21:51:38.595969

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bfbc77a8e4ae'
down_revision: Union[str, None] = '18237ea40f3f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuarios', sa.Column('email_normalizado', sa.String(length=256), nullable=False))
    op.create_index(op.f('ix_usuarios_email_normalizado'), 'usuarios', ['email_normalizado'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_usuarios_email_normalizado'), table_name='usuarios')
    op.drop_column('usuarios', 'email_normalizado')
    # ### end Alembic commands ###
