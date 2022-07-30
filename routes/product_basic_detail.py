from fastapi import APIRouter, Request
from sqlalchemy.sql import select
from config.db import conn, Base, engine
from models.index import product_basic_details, product_price_master
from schemas.index import ProductBasicDetail, AddProduct, ProductPrice, AddProductPrice, EditProductPrice
# EditMaterial

product_basic_detail = APIRouter()
@product_basic_detail.get("/product-details/{id}")
async def read_data(id: int):
    data = conn.execute(product_basic_details.select().where(product_basic_details.c.organization_id == id)).fetchall()
    return_data = []
    for item in data:
        obj = ProductBasicDetail(Id=item["id"], ProductCode=item["product_code"],ProductName=item["product_name"],
        ProductUnit=item["product_unit"],ProductGroupCode=item["product_group_code"])
        return_data.append(obj.dict())
    return {"organizationId": id, "ProductList": return_data}


@product_basic_detail.post("/add-product")
async def write_data(product_data: AddProduct):
    org_id = product_data.organizationId
    products = product_data.ProductList
    data = conn.execute(select([product_basic_details.c.product_code]).where(product_basic_details.c.organization_id == org_id)).fetchall()
    if data:
        old_material_group = data[-1][0]
    else:
        old_material_group = "PC0" + str(org_id) + "0000"
    for product in products:
        new_code = old_material_group[:3]+str(int(old_material_group[3:]) + 1)
        x = conn.execute(product_basic_details.insert().values(
            product_code= new_code,
            product_name= product["ProductName"],
            product_unit=product["ProductUnit"],
            product_group_code=product["ProductGroupCode"],
            organization_id=org_id
        ))
        product_id = x.lastrowid
        # print(product_id)
        if product["HSNCode"]:
            conn.execute(product_price_master.insert().values(
            product_id= product_id,
            product_price= product["ProductPrice"],
            hsn_code=product["HSNCode"],
            discount=product["ProductDiscount"],
            start_date=product["StartDate"],
            end_date=product["EndDate"]
            ))
        old_material_group = new_code
    return {"organizationId": org_id, "Msg": "done"}

# @material_basic_detail.post("/edit-material")
# async def write_data(material_data: EditMaterial):
#     _id = material_data.Id
#     material_name = material_data.MaterialName
#     material_unit = material_data.MaterialUnit
#     material_group_code = material_data.MaterialGroupCode
#     conn.execute(material_basic_details.update().where(
#         material_basic_details.c.id == _id).values(
#         material_name= material_name,
#         material_unit=material_unit,
#         material_group_code=material_group_code
#     ))
#     return {"organizationId": _id, "Msg": "done"}


@product_basic_detail.get("/product-price/{proudct_id}")
async def read_data(proudct_id: int):
    data = conn.execute(product_price_master.select().where(product_price_master.c.product_id == proudct_id)).fetchall()
    return_data = []
    for item in data:
        obj = ProductPrice(Id=item["id"], ProductPrice=item["product_price"],HSNCode=item["hsn_code"],
        ProductDiscount=item["discount"], StartDate=item["start_date"], EndDate=item["end_date"])
        return_data.append(obj.dict())
    # print(data)
    return {"ProductId": proudct_id, "ProductPriceList": return_data}


@product_basic_detail.post("/add-product-price/")
async def write_data(product_price_data: AddProductPrice):
    product_id = product_price_data.ProductId
    price = product_price_data.ProductPrice
    discount = product_price_data.ProductDiscount
    start_date = product_price_data.StartDate
    end_date = product_price_data.EndDate
    hsn_code = product_price_data.HSNCode
    conn.execute(product_price_master.insert().values(
            product_id= product_id,
            product_price= price,
            hsn_code=hsn_code,
            discount=discount,
            start_date=start_date,
            end_date=end_date
        ))
    return {"ProductId": product_id, "Msg": "done"}

@product_basic_detail.post("/edit-product-price")
async def write_data(product_price_data: EditProductPrice):
    _id = product_price_data.Id
    price = product_price_data.ProductPrice
    discount = product_price_data.ProductDiscount
    start_date = product_price_data.StartDate
    end_date = product_price_data.EndDate
    conn.execute(product_price_master.update().where(
        product_price_master.c.id == _id).values(
        product_price= price,
        discount=discount,
        start_date=start_date,
        end_date=end_date
    ))
    return {"ProductPriceId": _id, "Msg": "done"}
