from .item import Item
from textadventure.util import items_to_dict


class Inventory:
    def __init__(self, *items: Item):
        self.items = items_to_dict(items)

    def add(self, *items: Item):
        for item in items:
            if item.name not in self:
                self.items[item.name] = item

    def remove(self, *item_names: str):
        for name in item_names:
            if name in self:
                del self.items[name]

    def quantity(self, item_name: str):
        if item_name not in self:
            return 0

        return self[item_name].quantity

    def get(self, item_name):
        return self.items.get(item_name)

    def search(self, query):
        for item in self:
            if query in item.name:
                yield item

    def __getitem__(self, item):
        return self.items[item]

    def __contains__(self, item):
        return item in self.items

    def __iter__(self):
        yield from self.items.values()

    def __repr__(self):
        return repr(self.items)


inv = Inventory(
    Item('berries', 30, 1.25),
    Item('water', 20, 2),
    Item('chips', 10, 2.5)
)
