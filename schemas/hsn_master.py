from pydantic import BaseModel

class HsnMatser(BaseModel):
    HSNCode : str
    HSNDsecription : str
    TaxRate : str
