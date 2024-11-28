"""fixagain

Revision ID: 5457b5077730
Revises: 
Create Date: 2024-11-28 19:48:52.525533

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5457b5077730'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('program', schema=None) as batch_op:
        batch_op.add_column(sa.Column('department_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint('program_ibfk_1', type_='foreignkey')
        batch_op.create_foreign_key(None, 'department', ['department_id'], ['id'])
        batch_op.drop_column('faculty_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('program', schema=None) as batch_op:
        batch_op.add_column(sa.Column('faculty_id', mysql.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('program_ibfk_1', 'program', ['faculty_id'], ['id'])
        batch_op.drop_column('department_id')

    # ### end Alembic commands ###
