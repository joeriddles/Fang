from sqlalchemy import Column, Integer, String

from .db_base import Base


class DbHero(Base):
    __tablename__ = 'heroes'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, unique=True)
