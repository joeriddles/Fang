from typing import Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .hero import CreateHero, Hero
from .mock_heroes import HEROES


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


@app.get("/api/heroes/", response_model=list[Hero])
def list_heroes(name: Optional[str]=None) -> list[Hero]:
    if name is not None:
        name = name.casefold()
        return [
            hero
            for hero
            in HEROES
            if name in hero.name.casefold()
        ]
    else:
        return HEROES


@app.get("/api/heroes/{id}/", response_model=Hero)
def get_hero_by_id(id: int) -> Hero:
    try:
        hero = [
            hero
            for hero
            in HEROES
            if hero.id == id
        ][0]
    except KeyError:
        raise HTTPException(404, f"Hero with id={id} not found")
    else:
        return hero


@app.post("/api/heroes/", response_model=Hero)
def add_hero(create_hero: CreateHero) -> Hero:
    hero = Hero(
        id = _generate_hero_id(HEROES),
        **create_hero.dict(),
    )
    HEROES.append(hero)
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


def _generate_hero_id(heroes: list[Hero]) -> int:
    if len(heroes) > 0:
        next_hero_id = max([
            hero.id
            for hero
            in HEROES
        ]) + 1
    else:
        next_hero_id = 11
    return next_hero_id
