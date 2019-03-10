from contextlib import contextmanager

from sqlalchemy import create_engine, orm, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

# mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
#                             connector_to_use  user pass host      database
engine = create_engine('mysql+mysqlconnector://root:password@localhost/python')
Base = declarative_base(bind=engine)
Session = orm.sessionmaker(bind=engine)


def create_tables():
    Base.metadata.create_all()


@contextmanager
def transaction():
    session = Session()
    yield session
    session.commit()
    session.close()


class Balance(Base):
    __tablename__ = 'balance'

    id = Column(Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
    name: str = Column(String, nullable=False)
    bal: int = Column(Float, nullable=False, default=100)


create_tables()

with transaction() as db:
    b: Balance
    for b in db.query(Balance):
        print(b.id, b.name, b.bal)
