from snake_player import Position
from random import randint
import colors


class Apple:
    def __init__(self, limits, color=colors.red):
        self.color = colors.red
        self.x_max = limits[0]
        self.y_max = limits[1]
        self.position = Position(
            x=randint(0, self.x_max),
            y=randint(0, self.y_max)
        )

    def reset(self):
        self.position.x = randint(0, self.x_max)
        self.position.y = randint(0, self.y_max)

    @staticmethod
    def create_rand_apple_list(amount, color, limits):
        apple_list = []
        for x in range(amount):
            apple_list.append(Apple((limits[0], limits[1])))

        return apple_list
