from datetime import timedelta, datetime

from pygameutil import *


class Pattern:
    def __init__(self, name):
        self.name = name

    def draw(self, pos):
        pass

    def update(self):
        pass


class Circle(Pattern):
    def __init__(self, length):
        super().__init__('circle')

        self.angle = 0
        self.length = length
        self.color = Color('red')

    def update(self):
        self.angle += 1

        if random() <= .005:
            self.color = random_color()

    def draw(self, pos):
        draw_line(self.color, pos, (rdcos(pos.x, self.length, self.angle), rdsin(pos.y, self.length, self.angle)))


class Star(Pattern):
    def __init__(self, points, length):
        super().__init__('star')

        self.angles = [i for i in range(0, 361, 360 // (points * 2))]
        self.length = length
        self.short_length = length // 2
        self.color = random_color()
        self.color_change_delay = timedelta(seconds=.2)
        self.last_color_change = datetime.now()

    def update(self):
        for i, _ in enumerate(self.angles):
            self.angles[i] += .03

        if datetime.now() - self.last_color_change >= self.color_change_delay:
            self.color = random_color()
            self.last_color_change = datetime.now()

    def draw(self, pos):
        points = [
            (
                rdcos(pos.x, self.short_length if i and i % 2 else self.length, angle),
                rdsin(pos.y, self.short_length if i and i % 2 else self.length, angle)
            )
            for i, angle in enumerate(self.angles)
        ]

        draw_lines(self.color, False, points, 2)


setup()

star_length = 100
star_sides = 5

circle_pattern = Circle(100)
star_pattern = Star(star_sides, star_length)
fixed = []

p = star_pattern

while True:
    for e in get_events():
        check_quit(e)

        if get_mouse_down(e) == 1:
            fixed.append((Star(star_sides, randint(1, 100)), get_mouse_pos_vect()))

    fill_screen()

    for star, pos in fixed:
        star.update()
        star.draw(pos)

    if key_held(K_SPACE):
        fill_screen()

    mouse = get_mouse_pos_vect()

    p.update()
    p.draw(mouse)

    update()
