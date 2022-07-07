from pydantic import BaseModel

class OrganizationDetail(BaseModel):
    organization_id : int
    organization_name : str
    organization_address : str
