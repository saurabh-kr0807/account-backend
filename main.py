# main.py
from fastapi import FastAPI
import mysql.connector
from routes.index import organization_detail, hsn_master, material_group_masters, material_basic_detail, test, material_group_add


app = FastAPI()


app.include_router(organization_detail)
app.include_router(hsn_master)
app.include_router(material_group_masters)
app.include_router(material_basic_detail)
app.include_router(test)
app.include_router(material_group_add)
