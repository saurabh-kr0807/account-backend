from sqlalchemy import Table, Column
from config.db import meta
from sqlalchemy.sql.sqltypes import Integer, String

material_group_master = Table(
    "material_group_master", meta,
    Column('id', Integer, primary_key=True),
    Column('material_group_code', String(45)),
    Column('material_group_dsecription', String(100))
)
