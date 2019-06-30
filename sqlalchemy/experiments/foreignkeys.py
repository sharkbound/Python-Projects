from contextlib import contextmanager
from traceback import print_exc

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:memory:')
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)


@contextmanager
def session():
    s = Session()
    try:
        yield s
        s.commit()
    except Exception as e:
        print(f'error occurred: {e}')
        print_exc()
        s.rollback()
    finally:
        s.close()


class Bank(Base):
    __tablename__ = 'bank'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.balance'), nullable=False, unique=True)
    balance = Column(Integer, nullable=False, default=100)

    def __repr__(self):
        return f'<Bank user_id={self.user_id} balance={self.balance}>'


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    # balance = relationship('Bank', back_ref=)

    balance = Column(Integer, ForeignKey('bank.user_id'))
    a = relationship('Bank', backref=backref('users'))

    def __str__(self):
        return f'<User name={self.name} balance={self.balance}>'


Base.metadata.create_all()

name = 'james'
with session() as s:
    user = User(name=name)
    s.add(user)
    s.commit()

    s.add(Bank(user_id=user.id))
    print(user.balance)
    print(s.query(Bank).all())
