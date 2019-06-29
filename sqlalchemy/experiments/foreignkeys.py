from contextlib import contextmanager

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///database.sqlite')
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)


@contextmanager
def session():
    s = Session()
    try:
        yield s
        s.commit()
    except:
        s.rollback()
    finally:
        s.close()


class Bank(Base):
    __tablename__ = 'bank'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False, unique=True)
    balance = Column(Integer, nullable=False, default=100)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    balance = Column(Integer, ForeignKey(Bank.balance)).references(Bank.balance)

    def __str__(self):
        return f'{self.name} {self.balance.balance}'


Base.metadata.create_all()

name = 'a'
with session() as s:
    if s.query(exists().where(User.name == name)).scalar():
        print(s.query(User).filter(User.name == name).one())
    else:
        s.add(User(name=name))
