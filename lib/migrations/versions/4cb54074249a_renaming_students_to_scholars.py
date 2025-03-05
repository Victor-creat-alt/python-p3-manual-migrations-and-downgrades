"""Renaming students to scholars

Revision ID: 4cb54074249a
Revises: 791279dd0760
Create Date: 2025-03-05 08:34:01.713723

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4cb54074249a'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')
    pass


def downgrade() -> None:
    op.rename_table('scholars', 'students')
    pass
