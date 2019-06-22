from random import randint, randrange
from Icons.player import Player
from Icons.vampire import Vampire
from game import Game
from Config.config import WIDTH, ROWS

game = Game(Player((0, 0), 14), '.', *[Vampire((randrange(WIDTH), randrange(ROWS))) for _ in range(3)])

while game.player.fuel > 0:

    if len(game.vampires) == 0:
        print('\nYOU WIN')
        exit()

    game.update_board_icons()
    print('\n\n',game)

    game.play_round()

print('\nYOU LOSE')