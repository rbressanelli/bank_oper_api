"""update user cpf type

Revision ID: 5332b2d572f8
Revises: 
Create Date: 2022-07-12 09:16:40.588927

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "5332b2d572f8"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    user_table = op.create_table(
        "users",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("cpf", sa.String(length=100), nullable=False),
        sa.Column("birthDate", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("user_id"),
        sa.UniqueConstraint("cpf"),
    )
    op.create_table(
        "accounts",
        sa.Column("account_id", sa.Integer(), nullable=False),
        sa.Column("balance", sa.Float(), nullable=True),
        sa.Column("daily_withdraw_limit", sa.Float(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=True),
        sa.Column("account_type", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.user_id"],
        ),
        sa.PrimaryKeyConstraint("account_id"),
        sa.UniqueConstraint("user_id"),
    )
    op.create_table(
        "transactions",
        sa.Column("transaction_id", sa.Integer(), nullable=False),
        sa.Column("value", sa.Float(), nullable=False),
        sa.Column("transaction_date", sa.DateTime(), nullable=False),
        sa.Column("account_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["account_id"],
            ["accounts.account_id"],
        ),
        sa.PrimaryKeyConstraint("transaction_id"),
    )
    # ### end Alembic commands ###

    op.bulk_insert(
        user_table,
        [
            {"name": "Roberto", "cpf": "12345678900", "birthDate": "2001/01/15"},
            {"name": "Simone", "cpf": "12345678999", "birthDate": "1996/07/25"},
        ],
    )


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("transactions")
    op.drop_table("accounts")
    op.drop_table("users")
    # ### end Alembic commands ###
