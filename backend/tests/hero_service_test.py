import pytest
from sqlalchemy.orm.session import Session

from backend.db_base import DbBase
from backend.hero import Hero
from backend.hero_service import HeroService
from backend.settings import Settings


@pytest.fixture
def db(scope="function") -> Session:
    settings = Settings.parse_obj({ "db_uri": "sqlite:///test.db" })
    db_base = DbBase(settings, connect_args={"check_same_thread": False})
    return db_base.get_db()


def test__hero_service__list_heroes__no_name(db: Session):
    hero_service = HeroService(db)
    heroes = hero_service.list_heroes()
    assert heroes == [
        Hero(id=1, name="Middle Manager of Justice"),
        Hero(id=2, name="Code Cowboy"),
    ]

