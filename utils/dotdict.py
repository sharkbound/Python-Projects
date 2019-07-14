import json
from collections import OrderedDict


class DotDict(OrderedDict):
    _missing: 'DotDict' = None

    def __getattr__(self, item):
        return self[item]

    def __setattr__(self, key, value):
        self[key] = value

    def __missing__(self, key):
        if self.__class__._missing is None:
            self.__class__._missing = DotDict()
        return self.__class__._missing

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
