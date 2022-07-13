# main.py
from fastapi import FastAPI
import mysql.connector
from fastapi.middleware.cors import CORSMiddleware
from routes.index import organization_detail, hsn_master, material_group_masters, material_basic_detail, material_group_add


app = FastAPI()
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(organization_detail)
app.include_router(hsn_master)
app.include_router(material_group_masters)
app.include_router(material_basic_detail)
app.include_router(material_group_add)
