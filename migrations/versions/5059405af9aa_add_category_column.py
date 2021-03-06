"""add category column

Revision ID: 5059405af9aa
Revises: 
Create Date: 2020-04-15 14:59:28.779449

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5059405af9aa"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "collection", sa.Column("category", sa.String(length=64), nullable=True)
    )
    op.create_index(
        op.f("ix_collection_category"), "collection", ["category"], unique=False
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_collection_category"), table_name="collection")
    op.drop_column("collection", "category")
    # ### end Alembic commands ###
