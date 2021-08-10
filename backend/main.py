from backend.hero_service import HeroService
from typing import Optional

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from .db_base import Base
from .db_hero import DbHero
from .hero import CreateHero, Hero
from .mock_heroes import HEROES
from .settings import Settings


app = FastAPI()

origins = [
    "http://localhost:4200",
    "http://127.0.0.1:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

settings = Settings()

engine = create_engine(settings.db_uri)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_hero_service():
    db = get_db()
    hero_service = HeroService(db)
    return hero_service


    
@app.get("/api/heroes/", response_model=list[Hero])
def list_heroes(name: Optional[str]=None, hero_service: HeroService = Depends(get_hero_service)) -> list[Hero]:
    heroes = hero_service.list_heroes(name)
    return heroes


@app.get("/api/heroes/{id}/", response_model=Hero)
def get_hero_by_id(id: int, hero_service: HeroService = Depends(get_hero_service)) -> Hero:
    hero = hero_service.get_hero_by_id(id)
    if hero is None:
        raise HTTPException(404, f"Hero with id={id} not found")
    return hero


@app.post("/api/heroes/", response_model=Hero)
def add_hero(create_hero: CreateHero, hero_service: HeroService = Depends(get_hero_service)) -> Hero:
    hero = hero_service.create_hero(create_hero)
    return hero


@app.put("/api/heroes/{id}/", response_model=None)
def update_hero(update: Hero) -> None:
    try:
        hero_index = [
            index
            for index
            in range(len(HEROES))
            if HEROES[index].id == update.id
        ][0]
    except KeyError:
        raise HTTPException(404, f"Hero with id={update.id} not found")
    else:
        hero = Hero(**update)
        HEROES[hero_index] = hero


@app.delete("/api/heroes/{id}/", response_model=Hero)
def delete_hero(id: int) -> None:
    try:
        hero_index = [
            index
            for index
            in range(len(HEROES))
            if HEROES[index].id == id
        ][0]
    except KeyError:
        raise HTTPException(404, f"Hero with id={id} not found")
    else:
        hero = HEROES.pop(hero_index)
        return hero
