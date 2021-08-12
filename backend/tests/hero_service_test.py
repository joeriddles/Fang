import pytest
from sqlalchemy.orm.session import Session

from backend.db_base import DbBase
from backend.db_hero import DbHero
from backend.hero import Hero
from backend.hero_service import HeroService
from backend.settings import Settings


DB_HEROES = [
    DbHero(id=1, name="Middle Manager of Justice"),
    DbHero(id=2, name="Code Cowboy"),
]


@pytest.fixture
def db(scope="function") -> Session:
    settings = Settings.parse_obj({ "db_uri": "sqlite:///test.db" })
    db_base = DbBase(settings, connect_args={"check_same_thread": False})
    for db in db_base.get_db():
        db.add_all(DB_HEROES)
        db.commit()
        yield db


def test__hero_service__list_heroes__no_name(db: Session):
    hero_service = HeroService(db)
    heroes = hero_service.list_heroes()
    assert heroes == [
        Hero(id=1, name="Middle Manager of Justice"),
        Hero(id=2, name="Code Cowboy"),
    ]

