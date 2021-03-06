"""empty message

Revision ID: 0f33318b0f74
Revises: 9f2022ed7ed8
Create Date: 2018-03-05 17:27:22.586809

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f33318b0f74'
down_revision = '9f2022ed7ed8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profile', sa.Column('password', sa.String(length=255), nullable=True))
    op.create_unique_constraint(None, 'user_profile', ['password'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_profile', type_='unique')
    op.drop_column('user_profile', 'password')
    # ### end Alembic commands ###
