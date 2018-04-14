from models.game import Game
from util import load_extensions

load_extensions('rooms')

game = Game()
game.run()
