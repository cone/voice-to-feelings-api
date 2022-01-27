from typing import List, Optional

from pydantic import BaseModel


class RecordBase(BaseModel):
    voice_to_text: str


class RecordCreate(RecordBase):
    pass


class Record(RecordBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    name: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    records: List[Record] = []

    class Config:
        orm_mode = True