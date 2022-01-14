"""UpdateRewardsAwardedAsVarchar

Revision ID: 848d9def72dc
Revises: 62f9e82adaa6
Create Date: 2022-01-14 17:57:50.064610

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '848d9def72dc'
down_revision = '62f9e82adaa6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user_rewards', 'rewards_awarded',
               existing_type=mysql.BIGINT(),
               type_=sa.VARCHAR(length=50),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user_rewards', 'rewards_awarded',
               existing_type=sa.VARCHAR(length=50),
               type_=mysql.BIGINT(),
               existing_nullable=False)
    # ### end Alembic commands ###