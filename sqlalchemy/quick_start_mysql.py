from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, orm, Column, Integer, String, Float, exists
from contextlib import contextmanager

# pip install mysql-connector-python
# mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
#                             connector_to_use  user pass host      database
engine = create_engine('mysql+mysqlconnector://user:password@localhost/<dbname>')
Base = declarative_base(bind=engine)
Session = orm.sessionmaker(bind=engine)


@contextmanager
def transaction():
    session: orm.Session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
    finally:
        session.close()


class Account(Base):
    __tablename__ = 'accounts'

    id: int = Column(Integer, primary_key=True, nullable=False)
    name: str = Column(String(50), nullable=False)
    bal: int = Column(Integer, nullable=False, default=100)

    def __str__(self):
        return f'<{self.__class__.__name__} id={self.id} name={self.name!r} bal={self.bal}>'


def new_account(name, bal=100):
    return Account(name=name, bal=bal)


Base.metadata.create_all()

with transaction() as s:
    if not s.query(exists().where(Account.name == 'james')).scalar():
        print('creating user...')
        s.add(new_account('james'))
    else:
        print('user already exists')

with transaction() as s:
    for account in s.query(Account):
        account.bal += 1

with transaction() as s:
    print('user:', s.query(Account).filter(Account.name == 'james').one())
