from pydantic import BaseModel

class MaterialBasicDetail(BaseModel):
    ID : int
    MaterialName : str
    MaterialUnit: int
    MaterialGroupCode : str

