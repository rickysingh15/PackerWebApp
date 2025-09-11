"""create users table

Revision ID: fadd7cbd5341
Revises: 
Create Date: 2025-09-07 01:25:14.628348

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fadd7cbd5341'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table("users", sa.Column("id", sa.String(), default=sa.text("gen_random_uuid()")),
                    sa.Column("first_name", sa.String(), nullable=False),
                    sa.Column("last_name", sa.String(), nullable=False),
                    sa.Column("username", sa.String(), nullable=False, unique=True),
                    sa.Column("email", sa.String(), nullable=False, unique=True),
                    sa.Column("phone_number", sa.String(), nullable=True, unique=True),
                    sa.Column("password", sa.String(), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint("username"),
                    sa.UniqueConstraint("email"),
                    sa.UniqueConstraint("phone_number")
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("users")
    pass
