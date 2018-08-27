from fighter import *

fireball = Move('fb', 12, 'throws a flaming fireball at your opponent', 'fireball')
death = Move('death', 100000, 'causes instant death')
poke = Move('poke', 1, 'casually pokes the opponent')

p1 = Player('player', MoveSet(fireball, death, poke))
cpu = Fighter('CPU', MoveSet(fireball, poke))

fight = Fight(p1, cpu)

print(fight.start())
