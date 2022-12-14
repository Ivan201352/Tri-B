"""Update UserMed

Revision ID: 8c18b41382ed
Revises: 149846c75a1f
Create Date: 2022-11-14 13:53:55.359033

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c18b41382ed'
down_revision = '149846c75a1f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_posts'))
    )
    op.add_column('users_med', sa.Column('post_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_users_med_post_id_posts'), 'users_med', 'posts', ['post_id'], ['id'])
    data_upgrades()
    # ### end Alembic commands ###

def data_upgrades():
    table = sa.sql.table('posts', sa.sql.column('name', sa.String))

    op.bulk_insert(table,
        [
            { 'name': 'Администратор' },
            { 'name': 'Хирург' },
            { 'name': 'Терапевт' },
            { 'name': 'Педиатр' },
            { 'name': 'Врач-лаборант' },
        ]
    )

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_users_med_post_id_posts'), 'users_med', type_='foreignkey')
    op.drop_column('users_med', 'post_id')
    op.drop_table('posts')
    # ### end Alembic commands ###
