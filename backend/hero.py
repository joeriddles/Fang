from pydantic import BaseModel


class Hero(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class CreateHero(BaseModel):
    name: str
