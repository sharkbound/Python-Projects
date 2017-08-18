from random import randint

from Config.config import WIDTH, ROWS


class Game:
    def __init__(self, player, blank_symbol, *vampires):
        self.player = player
        self.vampires = vampires
        self.board = []
        self.line = blank_symbol * WIDTH
        self.blank_symbol = blank_symbol


        self.move_dict = {'s': (0, 1), 'w': (0, -1), 'a': (-1, 0), 'd': (1, 0)}
        self.reset_board()

    @property
    def filled_board(self):
        return [list(self.line) for _ in range(ROWS)]

    @property
    def free_spaces(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == self.blank_symbol:
                    yield (j, i)

    def set_board_icon(self, x, y, new_icon):
        self.board[y][x] = new_icon

    def reset_board(self):
        self.board = self.filled_board

    def update_board_icons(self):
        self.reset_board()
        # self.vampires = [v for v in self.vampires if not v.check_collision(self.player)]

        self.set_board_icon(self.player.X, self.player.Y, self.player.symbol)
        for v in self.vampires:
            self.set_board_icon(v.X, v.Y, v.symbol)

    def play_round(self):
        for m in input('\nEnter Moves: '):
            dir = self.move_dict.get(m, (0, 0))
            self.player.move_rel(dir[0], dir[1])

            # move vampires
            for v in self.vampires:
                v(self.free_spaces)

            self.vampires = [v for v in self.vampires if not v.check_collision(self.player)]
        self.player.fuel -= 1

    def __str__(self):
        return (f'{self.player.fuel}\n\n' +
                ('\n'.join(''.join(L) for L in self.board)))
