from math import radians, sin, cos


def apply_angle(angle, dist, *args):
    x, y = args[0] if len(args) == 1 else args
    return x + dist * radians(cos(angle)), y + dist * radians(sin(angle))


class Angle:
    __slots__ = 'angle', 'initial_angle', 'last'

    def __init__(self, initial_angle=0):
        self.initial_angle = initial_angle
        self.angle = initial_angle
        self.last = initial_angle

    def rotate(self, angle, relative=False):
        """
        rotates based on [angle], use floats for precise rotations
        """
        self.last = self.angle
        if relative:
            self.angle = (self.angle + angle) % 361
        else:
            self.angle = angle % 361

    def copy(self):
        inst = self.__class__(self.angle)
        inst.initial_angle, inst.last = self.initial_angle, self.last
        return inst

    def apply_to(self, pos, dist):
        try:
            x, y = pos
        except TypeError:
            x, y = pos.x, pos.y
        return x + dist * radians(cos(self.angle)), y + dist * radians(sin(self.angle))
