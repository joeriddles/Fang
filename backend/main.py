from typing import Optional
from fastapi import FastAPI
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


@app.get("/api/heroes", response_model=list[Hero])
def list_heroes(name: Optional[str]) -> list[Hero]:
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

