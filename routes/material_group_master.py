from fastapi import APIRouter
from sqlalchemy.sql import select
from config.db import conn
from models.index import material_group_master
from schemas.index import MaterialGroupMaster, AddMaterialGroupMaster

material_group_masters = APIRouter()
material_group_add = APIRouter()

@material_group_masters.get("/material-group/{id}")
async def read_data(id: int):
    data = conn.execute(material_group_master.select().where(material_group_master.c.organization_id == id)).fetchall()
    MaterialGroupList = []
    for item in data:
        obj = MaterialGroupMaster(MaterialGroupCode=item["material_group_code"], MaterialGroupDsecription=item["material_group_dsecription"])
        MaterialGroupList.append(obj.dict())
    return  MaterialGroupList


@material_group_add.post("/add-material-group")
async def write_data(material_group_data: AddMaterialGroupMaster):
    org_id = material_group_data.organizationId
    material_group_dsecription = material_group_data.MaterialGroupDsecription
    data = conn.execute(select([material_group_master.c.material_group_code]).where(material_group_master.c.organization_id == org_id)).fetchall()
    if data:
        old_material_group = data[-1][0]
    else:
        old_material_group = "MGC0" + str(org_id) + "000"
    MaterialGroupList = []
    new_code = old_material_group[:4]+str(int(old_material_group[4:]) + 1)
    conn.execute(material_group_master.insert().values(
            material_group_code=new_code,
            material_group_dsecription=material_group_dsecription,
            organization_id=org_id
        ))
    return_data = conn.execute(
        select(material_group_master.c.material_group_code,
        material_group_master.c.material_group_dsecription).where(
            material_group_master.c.organization_id == org_id)).fetchall()
    for item in return_data:
        obj = MaterialGroupMaster(MaterialGroupCode=item["material_group_code"], MaterialGroupDsecription=item["material_group_dsecription"])
        MaterialGroupList.append(obj.dict())
    return MaterialGroupList

