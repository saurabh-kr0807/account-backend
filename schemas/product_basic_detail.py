from pydantic import BaseModel

class ProductBasicDetail(BaseModel):
    Id : int
    ProductCode : str
    ProductName : str
    ProductUnit: int
    ProductGroupCode : str

class EditProduct(BaseModel):
    Id : int
    ProductName : str
    ProductUnit: int
    ProductGroupCode : str

class AddProduct(BaseModel):
    organizationId : int
    ProductList : list
