from pydantic import BaseModel

class MaterialBasicDetail(BaseModel):
    Id : int
    MaterialName : str
    MaterialUnit: int
    MaterialGroupCode : str

class EditMaterial(BaseModel):
    Id : int
    MaterialName : str
    MaterialUnit: int
    MaterialGroupCode : str
