from contextlib import contextmanager
import traceback
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref, lazyload

engine = create_engine('sqlite:///:memory:')
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()


@contextmanager
def transaction():
    try:
        yield session
        session.commit()
    except Exception:
        traceback.print_exc()
        session.rollback()


def new_id():
    return Column(Integer, primary_key=True, autoincrement=True, nullable=False)


USER_AND_TEAM = Table(
    'user_team_link', Base.metadata,
    Column('user_id', Integer(), ForeignKey('teams.name')),
    Column('team_name', Integer(), ForeignKey('users.team_name')),
)


class User(Base):
    __tablename__ = 'users'

    id: int = new_id()
    name: str = Column(String(255), nullable=False, unique=True)
    team_name: str = Column(String(255), ForeignKey('teams.name'), nullable=True)
    team: 'Team' = relationship('Team', backref=backref('b'))

    @classmethod
    def new(cls, name, team_name=None):
        user = cls(name=name, team_name=team_name)
        with transaction() as t:
            t.add(user)
        return user

    def __repr__(self):
        return f'<User name={self.name} team={self.team_name}>'


class Team(Base):
    __tablename__ = 'teams'

    id: int = new_id()
    name: str = Column(String(255), unique=True, nullable=False)
    members = relationship('User', backref=backref('b'))

    @classmethod
    def new(cls, name):
        team = cls(name=name)
        with transaction() as t:
            t.add(team)
        return team

    def __repr__(self):
        return f'<Team name={self.name}>'


Base.metadata.create_all()

Team.new('python')
Team.new('not-python')

User.new('james', 'python')
User.new('james2', 'python')
User.new('james3', 'python')
User.new('james4', 'not-python')

with transaction() as t:
    team: Team
    for team in t.query(Team):
        print(team.members)
    for user in t.query(User):
        print(user)

# stdout:
# [<User name=james team=python>, <User name=james2 team=python>, <User name=james3 team=python>]
# [<User name=james4 team=not-python>]
# <User name=james team=python>
# <User name=james2 team=python>
# <User name=james3 team=python>
# <User name=james4 team=not-python>
