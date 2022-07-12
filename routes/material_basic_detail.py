from fastapi import APIRouter, Request
from config.db import conn, Base
from models.index import material_basic_details
from schemas.index import MaterialBasicDetail, AddMaterial, EditMaterial

material_basic_detail = APIRouter()
@material_basic_detail.get("/material-details/{id}")
async def read_data(id: int):
    data = conn.execute(material_basic_details.select().where(material_basic_details.c.organization_id == id)).fetchall()
    return_data = []
    for item in data:
        obj = MaterialBasicDetail(Id=item["id"], MaterialName=item["material_name"], MaterialUnit=item["material_unit"],
                                MaterialGroupCode=item["material_group_code"])
        return_data.append(obj.dict())
    return {"organizationId": id, "MeterialList": return_data}


@material_basic_detail.post("/add-material")
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
    return {"organizationId": org_id, "Msg": "done"}

@material_basic_detail.post("/edit-material")
async def write_data(material_data: EditMaterial):
    _id = material_data.Id
    material_name = material_data.MaterialName
    material_unit = material_data.MaterialUnit
    material_group_code = material_data.MaterialGroupCode
    conn.execute(material_basic_details.update().where(
        material_basic_details.c.id == _id).values(
        material_name= material_name,
        material_unit=material_unit,
        material_group_code=material_group_code
    ))
    return {"organizationId": _id, "Msg": "done"}
