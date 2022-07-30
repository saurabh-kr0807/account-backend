from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional

class ProductPrice(BaseModel):
    Id : str
    ProductPrice : str
    ProductDiscount : str
    HSNCode : str
    StartDate : Optional[str] = ''
    EndDate : Optional[str] = ''


class AddProductPrice(BaseModel):
    ProductId : str
    ProductPrice : str
    ProductDiscount : str
    HSNCode : str
    StartDate : Optional[str] = ''
    EndDate : Optional[str] = ''

class EditProductPrice(BaseModel):
    Id : str
    ProductPrice : str
    ProductDiscount : str
    StartDate : Optional[str] = ''
    EndDate : Optional[str] = ''
