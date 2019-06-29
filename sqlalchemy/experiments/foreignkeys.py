from contextlib import contextmanager

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)


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
