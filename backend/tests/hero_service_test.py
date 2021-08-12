
from sqlalchemy.orm.session import Session

from backend.hero import CreateHero, Hero
from backend.hero_service import HeroService
from .fixtures import db


def test__hero_service__list_heroes__no_name(db: Session):
    hero_service = HeroService(db)
    heroes = hero_service.list_heroes()
    assert heroes == [
        Hero(id = 1, name = "Middle Manager of Justice"),
        Hero(id = 2, name = "Code Cowboy"),
    ]


def test__hero_service__list_heroes__name(db: Session):
    hero_service = HeroService(db)
    heroes = hero_service.list_heroes('Manager')
    assert heroes == [
        Hero(id = 1, name = "Middle Manager of Justice"),
    ]


def test__hero_service__get_hero_by_id(db: Session):
    hero_service = HeroService(db)
    heroe = hero_service.get_hero_by_id(2)
    assert heroe == Hero(id = 2, name = "Code Cowboy")


def test__hero_service__create_hero(db: Session):
    hero_service = HeroService(db)
    new_hero = CreateHero(name='Mad Scientist')
    hero = hero_service.create_hero(new_hero)
    assert hero == Hero(id = 3, name = 'Mad Scientist')


def test__hero_service__update_hero(db: Session):
    hero_service = HeroService(db)
    update = Hero(id = 2, name = 'Team Player')
    hero_service.update_hero(update)
    hero = hero_service.get_hero_by_id(2)
    assert hero == Hero(id = 2, name = 'Team Player')


def test__hero_service__delete_hero(db: Session):
    hero_service = HeroService(db)
    hero_service.delete_hero(2)
    assert hero_service.list_heroes() == [
        Hero(id = 1, name = 'Middle Manager of Justice')
    ]
