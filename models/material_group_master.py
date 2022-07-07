from sqlalchemy import Table, Column, ForeignKey
from config.db import meta
from sqlalchemy.sql.sqltypes import Integer, String

material_group_master = Table(
    "material_group_master", meta,
    Column('material_group_code', String(45),primary_key=True, nullable=False),
    Column('material_group_dsecription', String(100)),
    Column('organization_id', Integer, ForeignKey('organization_details.organization_id'), nullable=False),
)
