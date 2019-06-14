from random import choice


# for eso challenge : https://github.com/python-discord/esoteric-python-challenges/tree/master/challenges/06-maybe-keyword

class MaybeMeta(type):
    def __instancecheck__(self, instance):
        return type(self) is Maybe

    def __bool__(self):
        return choice([True, False])

    def __getattribute__(self, *args, **kwargs):
        if args[0] == '__class__':
            return True.__getattribute__(*args, **kwargs)
        return self.__dict__[args[0]]

    def __repr__(self):
        return str(choice([True, False]))

    def __set__(self, instance, value):
        print('set')


class Maybe(metaclass=MaybeMeta):
    pass


print(Maybe)  # will print True or False randomly.

if Maybe:
    print("And this code might run if it feels like it")

print(isinstance(Maybe, bool))  # will print True, always.

# and just to be consistent with other keywords...
Maybe = "hello!"  # this should raise a SyntaxError immediately, if possible.
