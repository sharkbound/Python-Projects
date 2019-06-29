from contextlib import contextmanager

from sqlalchemy import create_engine, String, DateTime, Integer, REAL, Float, BLOB, JSON, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

__all__ = [
    'String',
    'DateTime',
    'Integer',
    'Column',
    'REAL',
    'BLOB',
    'JSON',
    'get_engine',
    'get_session_maker',
    'init_tables',
    'Base',
    'sqlite_engine'
]

Base = declarative_base()
_engine = None
_Session = None


def get_engine():
    return _engine


def get_session_maker():
    global _Session
    if _Session is None:
        _Session = sessionmaker(bind=get_engine())

    return _Session


def init_tables():
    Base.metadata.create_all()


def sqlite_engine(in_memory=False, file='database.sqlite'):
    global _engine
    if in_memory:
        _engine = create_engine('sqlite:///:memory:')
    else:
        _engine = create_engine(f'sqlite:///{file}')

    return _engine


@contextmanager
def transaction():
    s = get_session_maker()()
    try:
        yield s
        s.commit()
    except:
        s.rollback()
    finally:
        s.close()
