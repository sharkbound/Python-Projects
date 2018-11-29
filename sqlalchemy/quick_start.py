from sqlalchemy import orm, create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from contextlib import contextmanager

# the base for all object to DB mapping classes
Base = declarative_base()

# engine that handles DB interaction            echo is for seeing what queries the engine is doing, can be set to False
engine = create_engine('sqlite:///database.db', echo=False)

# bind engine to the ORM Base
Base.metadata.bind = engine

# db session type
Session = orm.sessionmaker(bind=engine)

# db session instance
db: orm.Session = Session()


# object to DB row/column mapping class
# changes to class instances of User will translate to DB queries which can be commited
class User(Base):
    # name of the table for this class
    __tablename__ = 'users'

    # columns for the table
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    bal = Column(Integer, nullable=False, default=100)

    def __str__(self):
        return f'<User name={self.name!r} bal={self.bal}>'


# util function to make creating a new User easier ( to get around no init auto complete )
def new_user(name):
    return User(name=name)


# create all tables if not exists
Base.metadata.create_all()


@contextmanager
def transaction():
    yield
    db.commit()


# fetches a user
def get_user(name) -> User:
    return db.query(User).filter(User.name == name).one_or_none()


# create timmy if he is not in the db
if not get_user('timmy'):
    # shortcut for db.commit()
    with transaction():
        # add a new row in User for timmy
        db.add(new_user('timmy'))
        # the `with transaction()` automatically does the db.commit() for us here
        # otherwise we would need to do db.commit() after adding new rows / modifying rows

print(get_user('timmy'))
