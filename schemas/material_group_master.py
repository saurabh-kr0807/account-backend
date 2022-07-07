from pydantic import BaseModel

class MaterialGroupMaster(BaseModel):
    MaterialGroupCode : str
    MaterialGroupDsecription : str

class AddMaterialGroupMaster(BaseModel):
    organizationId : int    
    MaterialGroupDsecription : str
