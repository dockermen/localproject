"""update

Revision ID: f0bb0b659a44
Revises: 2f106d7fd125
Create Date: 2024-12-08 11:06:33.104351

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0bb0b659a44'
down_revision = '2f106d7fd125'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('VideoInfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('url', sa.String(length=128), nullable=True),
    sa.Column('url_key', sa.String(length=64), nullable=True),
    sa.Column('password', sa.String(length=64), nullable=True),
    sa.Column('createtime', sa.DateTime(), nullable=True),
    sa.Column('updatetime', sa.DateTime(), nullable=True),
    sa.Column('visitor_num', sa.Integer(), autoincrement=True, nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('student')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=64), nullable=True),
    sa.Column('url', sa.VARCHAR(length=128), nullable=True),
    sa.Column('url_key', sa.VARCHAR(length=64), nullable=True),
    sa.Column('password', sa.VARCHAR(length=64), nullable=True),
    sa.Column('createtime', sa.DATETIME(), nullable=True),
    sa.Column('updatetime', sa.DATETIME(), nullable=True),
    sa.Column('visitor_num', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('VideoInfo')
    # ### end Alembic commands ###
