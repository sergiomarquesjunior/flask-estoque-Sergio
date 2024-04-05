"""DataMixin

Revision ID: 18237ea40f3f
Revises: 742920380eac
Create Date: 2024-04-04 21:40:57.970189

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '18237ea40f3f'
down_revision: Union[str, None] = '742920380eac'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuarios', sa.Column('dta_cadastro', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False))
    op.add_column('usuarios', sa.Column('dta_atualizacao', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usuarios', 'dta_atualizacao')
    op.drop_column('usuarios', 'dta_cadastro')
    # ### end Alembic commands ###
