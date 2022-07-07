from sqlalchemy import Table, Column
from config.db import meta
from sqlalchemy.sql.sqltypes import Integer, String

organization_details = Table(
    "organization_details", meta,
    Column('organization_id', Integer, primary_key=True),
    Column('organization_name', String(45)),
    Column('organization_address', String(200)) 
)
