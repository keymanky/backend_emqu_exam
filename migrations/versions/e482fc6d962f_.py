"""empty message

Revision ID: e482fc6d962f
Revises: 
Create Date: 2024-02-24 20:01:47.542004

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e482fc6d962f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('computer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('ip', sa.String(length=70), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('ip')
    )
    op.create_table('ping',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ip', sa.String(length=70), nullable=True),
    sa.Column('result', sa.String(length=60), nullable=True),
    sa.Column('comment', sa.String(length=360), nullable=True),
    sa.Column('moment', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=60), nullable=True),
    sa.Column('lastname', sa.String(length=60), nullable=True),
    sa.Column('email', sa.String(length=70), nullable=True),
    sa.Column('password', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('ping')
    op.drop_table('computer')
    # ### end Alembic commands ###