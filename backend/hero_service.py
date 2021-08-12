from typing import Optional, Union

from sqlalchemy.orm.session import Session
from .db_hero import DbHero
from .hero import CreateHero, Hero


class HeroService:
    
    def __init__(self, db: Session):
        self.db = db

    def list_heroes(self, name: Optional[str]=None) -> list[Hero]:
        if name is not None:
            name_filter = f'%{name}%'
            db_heroes = self.db.query(DbHero).filter(DbHero.name.ilike(name_filter))
        else:
            db_heroes = self.db.query(DbHero).all()
        heroes = [
            Hero.from_orm(db_hero)
            for db_hero
            in db_heroes
        ]
        return heroes

    def get_hero_by_id(self, id: int) -> Union[Hero, None]:
        hero = None
        db_hero = self.db.query(DbHero).get(id)
        if db_hero is not None:
            hero = Hero.from_orm(db_hero)
        return hero

    def create_hero(self, create_hero: CreateHero) -> Hero:
        db_hero = DbHero(**create_hero.dict())
        self.db.add(db_hero)
        self.db.commit()
        self.db.refresh(db_hero)
        created_hero = Hero.from_orm(db_hero)
        return created_hero

    def update_hero(self, update: Hero):
        update_count = self.db.query(DbHero) \
            .filter(DbHero.id == update.id) \
            .update(update.dict(exclude={ 'id' }))
        self.db.commit()
        if update_count == 0:
            raise ValueError(id)

    def delete_hero(self, id: int):
        db_hero = self.db.query(DbHero).get(id)
        if db_hero is None:
            raise ValueError(id)
        self.db.delete(db_hero)
        self.db.commit()
