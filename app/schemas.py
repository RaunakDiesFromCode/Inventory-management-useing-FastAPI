from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None


class ItemResponse(Item):
    id: int

    class Config:
        orm_mode = True
