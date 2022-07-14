"""Update index on user balance snapshot table.

Revision ID: 7ebcbe8dcfa1
Revises: 7f844b08e3c9
Create Date: 2022-07-13 16:14:18.347613

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7ebcbe8dcfa1'
down_revision = '7f844b08e3c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('window_snapshotguid_addr_idx', 'user_balance_snapshot', ['airdrop_window_id', 'snapshot_guid', 'address'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('window_snapshotguid_addr_idx', table_name='user_balance_snapshot')
    # ### end Alembic commands ###