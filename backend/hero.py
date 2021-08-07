from pydantic import BaseModel


class Hero(BaseModel):
    id: int
    name: str


class CreateHero(BaseModel):
    name: str
