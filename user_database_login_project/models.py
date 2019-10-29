import traceback
from contextlib import contextmanager
from hashlib import sha3_512
from typing import Optional

from sqlalchemy import create_engine, Column, String, exists
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db.sqlite')
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()


def hash_password(password, salt='SALT'):
    sha = sha3_512()
    sha.update((salt + password + salt).encode())
    return sha.hexdigest()


def standardize(*texts):
    return (text.strip().lower() for text in texts)


class User(Base):
    __tablename__ = 'users'

    username: str = Column(String(50), primary_key=True, nullable=False, unique=True)
    pass_hash: str = Column(String(128), nullable=False)

    @classmethod
    def new(cls, username, password, commit=True) -> 'User':
        username, password = standardize(username, password)

        with transaction() as t:
            user = User(username=username, pass_hash=hash_password(password))
            if commit and not cls.exists(username):
                t.add(user)
            return user

    @classmethod
    def exists(cls, username) -> bool:
        username, = standardize(username)
        with transaction() as t:
            return t.query(exists().where(User.username == username)).scalar()

    @classmethod
    def get(cls, username) -> Optional['User']:
        username, = standardize(username)
        with transaction() as t:
            return t.query(User).filter(User.username == username).one_or_none()

    def __repr__(self):
        return f'<User username={self.username!r}>'


Base.metadata.create_all()


@contextmanager
def transaction():
    s = Session()
    try:
        yield s
        s.commit()
    except Exception:
        traceback.print_exc()
        s.rollback()
    finally:
        s.close()


with transaction() as t:
    # user = User.new('timmy', 'timmy')
    # t.commit()
    print(User.get('timmy'))
