from pydantic import BaseModel

class ProductGroupMaster(BaseModel):
    ProductGroupCode : str
    ProductGroupDsecription : str

class AddProductGroupMaster(BaseModel):
    organizationId : int    
    ProductGroupDsecription : str
