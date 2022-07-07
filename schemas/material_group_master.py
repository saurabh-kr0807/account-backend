from pydantic import BaseModel

class MaterialGroupMaster(BaseModel):
    ID : int
    MaterialGroupCode : str
    MaterialGroupDsecription : str
