"""empty message

Revision ID: efeddaf2c98f
Revises: 29c864696606
Create Date: 2024-12-08 12:02:21.739908

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'efeddaf2c98f'
down_revision = '29c864696606'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('VideoInfo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('visitor_num', sa.Integer(), autoincrement=True, nullable=True))
        batch_op.drop_column('visit_count')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('VideoInfo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('visit_count', sa.INTEGER(), nullable=True))
        batch_op.drop_column('visitor_num')

    # ### end Alembic commands ###
