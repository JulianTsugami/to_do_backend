from pydantic import BaseModel


class Item(BaseModel):
    id: int
    note: str

    class Config:
        orm_mode = True


class ItemCreate(BaseModel):
    note: str

class ItemUpdate(BaseModel):
    note: str