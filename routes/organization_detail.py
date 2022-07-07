from fastapi import APIRouter
from config.db import conn
from models.index import organization_details
from schemas.index import OrganizationDetail

organization_detail = APIRouter()

@organization_detail.get("/")
async def read_data():
    return conn.execute(organization_details.select()).fetchall()
