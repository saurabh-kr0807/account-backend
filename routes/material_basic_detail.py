from fastapi import APIRouter, Request
from config.db import conn, Base
from models.index import material_basic_details
from schemas.index import MaterialBasicDetail, AddMaterial

material_basic_detail = APIRouter()
test = APIRouter()
@material_basic_detail.get("/material-details/{id}")
async def read_data(id: int):
    data = conn.execute(material_basic_details.select().where(material_basic_details.c.organization_id == id)).fetchall()
    # data = conn.execute("SELECT organization_id from material_basic_details")
    return_data = []
    for item in data:
        obj = MaterialBasicDetail(ID=item["id"], MaterialName=item["material_name"], MaterialUnit=item["material_unit"],
                                MaterialGroupCode=item["material_group_code"])
        return_data.append(obj.dict())
    return {"organizationId": id, "MeterialList": return_data}


@test.post("/add-material")
async def write_data(material_data: AddMaterial):
    org_id = material_data.organizationId
    materials = material_data.materialList
    for material in materials:
        conn.execute(material_basic_details.insert().values(
            material_name= material["MaterialName"],
            material_unit=material["MaterialUnit"],
            material_group_code=material["MaterialGroupCode"],
            organization_id=org_id
        ))
    return material_data
