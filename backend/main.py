from backend.settings import Settings
from starlette.responses import Response
from backend.hero_service import HeroService
from typing import Optional

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm.session import Session

from .db_base import DbBase
from .hero import CreateHero, Hero


app = FastAPI()

origins = [
    "http://localhost:4200",
    "http://127.0.0.1:4200",
    "http://frontend:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

settings = Settings()
db_base = DbBase(settings)


@app.get(
    "/api/heroes/",
    response_model=list[Hero]
)
def list_heroes(name: Optional[str]=None, db: Session = Depends(db_base.get_db)) -> list[Hero]:
    hero_service = HeroService(db)
    heroes = hero_service.list_heroes(name)
    return heroes


@app.get(
    "/api/heroes/{id}/",
    response_model=Hero
)
def get_hero_by_id(id: int, db: Session = Depends(db_base.get_db)) -> Hero:
    hero_service = HeroService(db)
    hero = hero_service.get_hero_by_id(id)
    if hero is None:
        raise_404(id)
    return hero


@app.post(
    "/api/heroes/",
    response_model=Hero
)
def add_hero(create_hero: CreateHero, db: Session = Depends(db_base.get_db)) -> Hero:
    hero_service = HeroService(db)
    hero = hero_service.create_hero(create_hero)
    return hero


@app.put(
    "/api/heroes/{id}/",
    response_model=None,
    response_class=Response,
    status_code=204,
)
def update_hero(id: int, update: Hero, db: Session = Depends(db_base.get_db)) -> None:
    hero_service = HeroService(db)
    try:
        hero_service.update_hero(id, update)
    except ValueError:
        raise_404(id)


@app.delete(
    "/api/heroes/{id}/",
    response_model=None,
    response_class=Response,
    status_code=204,
)
def delete_hero(id: int, db: Session = Depends(db_base.get_db)) -> None:
    hero_service = HeroService(db)
    hero_service.delete_hero(id)


def raise_404(id: int):
    raise HTTPException(404, f"Hero with id={id} not found")
