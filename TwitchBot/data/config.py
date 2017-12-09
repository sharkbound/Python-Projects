import json
import os

class Config:
    def __init__(self, filename, foldername='Config', **kwargs):
        self.data = kwargs
        self.foldername = foldername
        self.filename = filename

        if not os.path.exists(self.foldername):
            os.mkdir(self.foldername)

        if os.path.exists(self.rel_path):
            self.load()
        else:
            self.save()

    @property
    def rel_path(self):
        return os.path.join(self.foldername, self.filename)

    @property
    def abs_path(self):
        return os.path.join(os.getcwd(), self.foldername, self.filename)

    def save(self):
        with open(self.rel_path, 'w') as sf:
            json.dump(self.data, sf, indent=2)

    def load(self):
        with open(self.rel_path) as lf:
            self.data = json.load(lf)

    def __iter__(self):
        yield from self.data.items()

    def __getitem__(self, item):
        return self.data.get(item)

    def __setitem__(self, key, value):
        self.data[key] = value
        self.save()

    def __delitem__(self, key):
        del self.data[key]
        self.save()
