from fastapi import APIRouter
from config.db import conn
from models.index import material_group_master
from schemas.index import MaterialGroupMaster

material_group_masters = APIRouter()

@material_group_masters.get("/material-group")
async def read_data():
    data = conn.execute(material_group_master.select()).fetchall()
    return_data = []
    for item in data:
        obj = MaterialGroupMaster(ID=item["id"], MaterialGroupCode=item["material_group_code"], MaterialGroupDsecription=item["material_group_dsecription"])
        return_data.append(obj.dict())
    return return_data
