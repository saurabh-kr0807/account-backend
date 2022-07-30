from sqlalchemy import Table, Column, ForeignKey
from config.db import meta
from sqlalchemy.sql.sqltypes import Integer, String
# from models.index import organization_details

product_basic_details = Table(
    "product_basic_details", meta,
    Column('id', Integer, primary_key=True),
    Column('product_code', String(45)),
    Column('product_name', String(45)),
    Column('product_unit', Integer),
    Column('product_group_code', String(45), ForeignKey('product_group_master.product_group_code'), nullable=False),
    Column('organization_id', Integer, ForeignKey('organization_details.organization_id'), nullable=False),
)
