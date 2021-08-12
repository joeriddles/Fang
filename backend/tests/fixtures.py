import os

import pytest

from backend.db_base import DbBase
from backend.db_hero import DbHero
from backend.files import TOP_LEVEL_DIR
from backend.settings import Settings


@pytest.fixture
def db():
    # Remove test.db if it exists
    sql_file = os.path.abspath(os.path.join(TOP_LEVEL_DIR, "test.db"))
    if os.path.exists(sql_file):
        os.remove(sql_file)

    db_heroes = [
        DbHero(id = 1, name = "Middle Manager of Justice"),
        DbHero(id = 2, name = "Code Cowboy"),
    ]

    settings = Settings.parse_obj({ "db_uri": "sqlite:///test.db" })
    db_base = DbBase(settings, connect_args={"check_same_thread": False})
    for db in db_base.get_db():
        db.add_all(db_heroes)
        db.commit()
        yield db
    
    # Clean up test.db
    sql_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "test.db"))
    os.remove(sql_file)
