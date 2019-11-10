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
session = None


def hash_password(password, salt='SALT'):
    sha = sha3_512()
    sha.update(normalize(f'{salt}{password}{salt}').encode())
    return sha.hexdigest()


def normalize(*texts):
    if len(texts) == 1:
        return texts[0].strip().lower()
    return (text.strip().lower() for text in texts)


class User(Base):
    __tablename__ = 'users'

    username: str = Column(String(50), primary_key=True, nullable=False, unique=True)
    password: str = Column(String(128), nullable=False)

    def verify(self, password, salt='SALT'):
        password = normalize(password)
        return self.password == hash_password(password, salt=salt)

    def ask_and_verify(self, prompt, bad_password='password did not match the password on the account'):
        verified = self.verify(input(prompt))
        if not verified:
            print(bad_password)
        return verified

    @classmethod
    def new(cls, username, password, commit=True) -> 'User':
        username, password = normalize(username, password)

        with transaction() as t:
            user = User(username=username, password=hash_password(password))
            if commit and not cls.exists(username):
                t.add(user)
            return user

    @classmethod
    def exists(cls, username) -> bool:
        username = normalize(username)
        with transaction() as t:
            return t.query(exists().where(User.username == username)).scalar()

    @classmethod
    def get(cls, username) -> Optional['User']:
        username = normalize(username)
        with transaction() as t:
            return t.query(User).filter(User.username == username).one_or_none()

    def __repr__(self):
        return f'<User {self.username=!r}>'


Base.metadata.create_all()


@contextmanager
def transaction():
    global session

    if session is None:
        session = Session()

    try:
        yield session
        session.commit()
    except Exception:
        traceback.print_exc()
        session.rollback()


@contextmanager
def new_transaction():
    session = Session()

    try:
        yield session
        session.commit()
    except Exception:
        traceback.print_exc()
        session.rollback()
    finally:
        session.close()
