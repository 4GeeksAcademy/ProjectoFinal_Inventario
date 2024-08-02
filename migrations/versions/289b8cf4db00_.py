"""empty message

Revision ID: 289b8cf4db00
Revises: dcbb8d5e36a9
Create Date: 2024-07-30 17:31:40.414393

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '289b8cf4db00'
down_revision = 'dcbb8d5e36a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('address', schema=None) as batch_op:
        batch_op.add_column(sa.Column('customer', sa.Integer(), nullable=True))
        batch_op.drop_constraint('address_costumer_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'customer', ['customer'], ['nit'])
        batch_op.drop_column('costumer')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('address', schema=None) as batch_op:
        batch_op.add_column(sa.Column('costumer', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('address_costumer_fkey', 'customer', ['costumer'], ['nit'])
        batch_op.drop_column('customer')

    # ### end Alembic commands ###