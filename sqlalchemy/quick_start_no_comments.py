from sqlalchemy import orm, create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from contextlib import contextmanager

Base = declarative_base()
engine = create_engine('sqlite:///database.db', echo=False)
Base.metadata.bind = engine
Session = orm.sessionmaker(bind=engine)
db: orm.Session = Session()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    bal = Column(Integer, nullable=False, default=100)

    def __str__(self):
        return f'<User name={self.name!r} bal={self.bal}>'


def new_user(name):
    return User(name=name)


Base.metadata.create_all()


@contextmanager
def transaction():
    yield
    db.commit()


def get_user(name) -> User:
    return db.query(User).filter(User.name == name).one_or_none()


if not get_user('timmy'):
    with transaction():
        db.add(new_user('timmy'))

print(get_user('timmy'))
