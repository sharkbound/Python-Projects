from contextlib import contextmanager

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# create a engine to execute sql queries
# for a file, use file.sqlite instead of :memory:
engine = create_engine('sqlite:///:memory:')

# super class base for all table models
Base = declarative_base(bind=engine)

# session generator
Session = sessionmaker(bind=engine)


class Cookie(Base):
    __tablename__ = 'cookies'

    id: int = Column(Integer, primary_key=True)
    type: str = Column(String(255), nullable=False)


def init_tables():
    # creates all tables for models, if they do not exist
    Base.metadata.create_all()


init_tables()


@contextmanager
def transaction():
    s = Session()
    try:
        yield s
        s.commit()
    except:
        s.rollback()
    finally:
        s.close()


with transaction() as t:
    t.add(Cookie(type='test'))
