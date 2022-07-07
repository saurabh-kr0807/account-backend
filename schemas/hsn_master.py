from pydantic import BaseModel

class HsnMatser(BaseModel):
    ID : int
    HSNCode : str
    HSNDsecription : str
    TaxRate : str
