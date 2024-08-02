"""empty message

Revision ID: ce19d34a0aba
Revises: b5d491db5e6d
Create Date: 2024-08-02 22:10:12.183563

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce19d34a0aba'
down_revision = 'b5d491db5e6d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('address', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('nit_customer', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('nit_provider', sa.Integer(), nullable=True))
        batch_op.drop_constraint('address_nit_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'customer', ['nit_customer'], ['nit'])
        batch_op.create_foreign_key(None, 'provider', ['nit_provider'], ['nit'])
        batch_op.drop_column('nit')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('address', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nit', sa.INTEGER(), autoincrement=True, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('address_nit_fkey', 'customer', ['nit'], ['nit'])
        batch_op.drop_column('nit_provider')
        batch_op.drop_column('nit_customer')
        batch_op.drop_column('id')

    # ### end Alembic commands ###
