"""empty message

Revision ID: 913e886610dd
Revises: 
Create Date: 2020-08-04 11:15:44.522858

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '913e886610dd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('age', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employee')
    # ### end Alembic commands ###
