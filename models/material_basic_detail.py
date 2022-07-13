from sqlalchemy import Table, Column, ForeignKey
from config.db import meta
from sqlalchemy.sql.sqltypes import Integer, String
# from models.index import organization_details

material_basic_details = Table(
    "material_basic_details", meta,
    Column('id', Integer, primary_key=True),
    Column('material_code', String(45)),
    Column('material_name', String(45)),
    Column('material_unit', Integer),
    Column('material_group_code', String(45), ForeignKey('material_group_master.material_group_code'), nullable=False),
    Column('organization_id', Integer, ForeignKey('organization_details.organization_id'), nullable=False),
)
