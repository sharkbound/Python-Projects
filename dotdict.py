import json
from collections import OrderedDict


class DotDict(OrderedDict):
    def __getattr__(self, item):
        if item in self.__dict__:
            return self.__dict__[item]

        if item not in self:
            self[item] = DotDict()
            return self[item]

        return self[item]

    def __setattr__(self, key, value):
        self[key] = value

    def __missing__(self, key):
        self[key] = DotDict()
        return self[key]

    @property
    def json(self):
        return json.dumps(self)

# testing code
if __name__ == '__main__':
    d = DotDict()
    jimmy = d.jimmy
    jimmy.age, jimmy.name = 1, 'jimmy'
    d['jimmy']['friends'] = [1, 2, 3]

    print(d)
    print(d.json)