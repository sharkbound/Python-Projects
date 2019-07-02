from contextlib import contextmanager
from traceback import print_exc

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:memory:')
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)


def auto_str(cls):
    def __str__(self):
        values = ' '.join(f'{k}={v!r}' for k, v in self.__dict__.items() if not k.startswith('_'))
        return f'<{self.__class__.__name__} {values}>'

    cls.__str__ = __str__
    return cls


def new_id():
    return Column(Integer, primary_key=True)


@contextmanager
def session():
    s = Session()
    try:
        yield s
        s.commit()
    except Exception as e:
        raise
    finally:
        s.close()


class Weapon(Base):
    def __init__(self, id):
        super().__init__(id=id)

    __tablename__ = 'weapons'

    id = Column(String(255), primary_key=True)
    users = relationship('Player')

    def __repr__(self):
        return f'<Weapon {self.id}>'


class Armor(Base):
    def __init__(self, id):
        super().__init__(id=id)

    __tablename__ = 'armors'

    id = Column(String(255), primary_key=True)
    users = relationship('Player')

    def __repr__(self):
        return f'<Armor {self.id}>'


class Player(Base):
    def __init__(self, name, weapon_id=None, armor_id=None):
        super().__init__(name=name, weapon_id=weapon_id, armor_id=armor_id)

    __tablename__ = 'players'

    id = new_id()
    name = Column(String(255), nullable=False, unique=True)
    weapon_id = Column(String(255), ForeignKey('weapons.id'), nullable=True)
    armor_id = Column(String(255), ForeignKey('armors.id'), nullable=True)

    weapon: 'Weapon' = relationship('Weapon')
    armor: 'Armor' = relationship('Armor')

    def __repr__(self):
        return f'<Player {self.name}>'

    def __str__(self):
        return f'<Player name={self.name!r} weapon_id={self.weapon_id!r} weapon={self.weapon!r} armor_id={self.armor_id!r} armor={self.armor!r}>'


Base.metadata.create_all()

with session() as s:
    for weapon in ('axe', 'spear', 'pike', 'sword'):
        s.add(Weapon(weapon))

    for armor in ('dragon', 'melee', 'magic', 'summoner'):
        s.add(Armor(armor))

p = Player('james', armor_id='dragon')
p2 = Player('james2', armor_id='melee')

with session() as s:
    s.add(p)
    s.add(p2)
    s.commit()

    print(p)
    print(p2)
