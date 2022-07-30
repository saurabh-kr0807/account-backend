from sqlalchemy import Table, Column, ForeignKey
from config.db import meta
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Boolean
# from models.index import organization_details

product_price_master = Table(
    "product_price_master", meta,
    Column('id', Integer, primary_key=True),
    Column('product_id', Integer, ForeignKey('product_basic_details.id'), nullable=False),
    Column('product_price', String(45)),
    Column('hsn_code', String(45), ForeignKey('hsn_master.hsn_code'), nullable=False),
    Column('discount', String(45)),
    Column('start_date', DateTime),
    Column('end_date', DateTime),
    Column('active', Boolean),
)
