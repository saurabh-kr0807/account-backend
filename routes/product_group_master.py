from fastapi import APIRouter
from sqlalchemy.sql import select
from config.db import conn
from models.index import product_group_master
from schemas.index import ProductGroupMaster, AddProductGroupMaster

product_group_masters = APIRouter()
product_group_add = APIRouter()

@product_group_masters.get("/product-group/{id}")
async def read_data(id: int):
    data = conn.execute(product_group_master.select().where(product_group_master.c.organization_id == id)).fetchall()
    ProductGroupList = []
    for item in data:
        obj = ProductGroupMaster(ProductGroupCode=item["product_group_code"], ProductGroupDsecription=item["product_group_dsecription"])
        ProductGroupList.append(obj.dict())
    return  ProductGroupList

@product_group_add.post("/add-product-group")
async def write_data(product_group_data: AddProductGroupMaster):
    org_id = product_group_data.organizationId
    product_group_dsecription = product_group_data.ProductGroupDsecription
    data = conn.execute(select([product_group_master.c.product_group_code]).where(product_group_master.c.organization_id == org_id)).fetchall()
    if data:
        old_product_group = data[-1][0]
    else:
        old_product_group = "PGC0" + str(org_id) + "000"
    ProductGroupList = []
    new_code = old_product_group[:4]+str(int(old_product_group[4:]) + 1)
    conn.execute(product_group_master.insert().values(
            product_group_code=new_code,
            product_group_dsecription=product_group_dsecription,
            organization_id=org_id
        ))
    return_data = conn.execute(
        select(product_group_master.c.product_group_code,
        product_group_master.c.product_group_dsecription).where(
            product_group_master.c.organization_id == org_id)).fetchall()
    for item in return_data:
        obj = ProductGroupMaster(ProductGroupCode=item["product_group_code"], ProductGroupDsecription=item["product_group_dsecription"])
        ProductGroupList.append(obj.dict())
    return ProductGroupList
