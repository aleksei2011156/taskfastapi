from typing import List, Union, Optional
from pydantic import BaseModel


class HistoryBase(BaseModel):
    title: str
    description: Union[str, None] = None


class HistoryCreate(HistoryBase):
    name: int
    type: int
    count: int
    status: Optional[bool] = None


class History(HistoryBase):
    id: int
    name: int
    type: int
    count: int
    status: bool

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    pass


class User(UserBase):
    id: int
    name: str
    balance: int

    class Config:
        orm_mode = True