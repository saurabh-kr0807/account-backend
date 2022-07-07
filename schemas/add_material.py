from pydantic import BaseModel

class AddMaterial(BaseModel):
    organizationId : int
    materialList : list
