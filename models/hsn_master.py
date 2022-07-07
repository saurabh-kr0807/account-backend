from sqlalchemy import Table, Column
from config.db import meta
from sqlalchemy.sql.sqltypes import Integer, String

hsn_masters = Table(
    "hsn_master", meta,
    Column('id', Integer, primary_key=True),
    Column('hsn_code', String(45)),
    Column('hsn_dsecription', String(100)),
    Column('tax_rate', String(45)) 
)
