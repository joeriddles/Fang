from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from .settings import Settings


Base = declarative_base()


class DbBase:

    def __init__(self, settings: Settings, **kwargs):
        engine = create_engine(settings.db_uri, **kwargs)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        Base.metadata.create_all(bind=engine)
        self.SessionLocal = SessionLocal

    def get_db(self) -> Session:
        db: Session = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()
