from fastapi import APIRouter
from config.db import conn
from models.index import hsn_masters
from schemas.index import HsnMatser

hsn_master = APIRouter()

@hsn_master.get("/hsn")
async def read_data():
    data = conn.execute(hsn_masters.select()).fetchall()
    return_data = []
    for item in data:
        obj = HsnMatser(HSNCode=item["hsn_code"], HSNDsecription=item["hsn_dsecription"], TaxRate=item["tax_rate"])
        return_data.append(obj.dict())
    return return_data
