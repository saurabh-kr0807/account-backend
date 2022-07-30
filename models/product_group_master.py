from sqlalchemy import Table, Column, ForeignKey
from config.db import meta
from sqlalchemy.sql.sqltypes import Integer, String

product_group_master = Table(
    "product_group_master", meta,
    Column('product_group_code', String(45),primary_key=True, nullable=False),
    Column('product_group_dsecription', String(100)),
    Column('organization_id', Integer, ForeignKey('organization_details.organization_id'), nullable=False),
)
