"""empty message

Revision ID: 29c864696606
Revises: f0bb0b659a44
Create Date: 2024-12-08 11:56:56.020760

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29c864696606'
down_revision = 'f0bb0b659a44'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('VideoInfo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('visit_count', sa.Integer(), autoincrement=True, nullable=True))
        batch_op.drop_column('visitor_num')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('VideoInfo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('visitor_num', sa.INTEGER(), nullable=True))
        batch_op.drop_column('visit_count')

    # ### end Alembic commands ###