"""empty message

Revision ID: 010a6115b941
Revises: 50f84679e8ef
Create Date: 2024-07-30 15:06:19.107285

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '010a6115b941'
down_revision = '50f84679e8ef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address',
    sa.Column('nit', sa.Integer(), nullable=False),
    sa.Column('address', sa.String(length=60), nullable=False),
    sa.Column('city', sa.String(length=60), nullable=False),
    sa.Column('country', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('nit')
    )
    with op.batch_alter_table('customer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'address', ['id'], ['nit'])
        batch_op.drop_column('idAddr')

    with op.batch_alter_table('provider', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'address', ['id'], ['nit'])
        batch_op.drop_column('idAddr')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('provider', schema=None) as batch_op:
        batch_op.add_column(sa.Column('idAddr', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('id')

    with op.batch_alter_table('customer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('idAddr', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('id')

    op.drop_table('address')
    # ### end Alembic commands ###