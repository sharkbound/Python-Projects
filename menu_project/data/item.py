import locale

from constants import ITEM_INFO_ROW_FORMAT, ITEM_NAME_LENGTH, ITEM_BRAND_LENGTH, ITEM_INFO_HEADER
from textadventure.util import truncate

locale.setlocale(locale.LC_ALL, '')


class Item:
    def __init__(self, name, quantity, price, brand=''):
        self.brand = brand
        self.price = price
        self.quantity = quantity
        self.name = name

    @property
    def total_cost(self):
        return self.quantity * self.price

    @property
    def total_cost_formatted(self):
        return locale.currency(self.total_cost)

    @property
    def price_formatted(self):
        return locale.currency(self.price)


def print_item_row(item: Item):
    print(ITEM_INFO_ROW_FORMAT.format(
        truncate(item.name, ITEM_NAME_LENGTH),
        truncate(item.brand, ITEM_BRAND_LENGTH),
        item.quantity,
        item.price_formatted))


def show_item_table(*items: Item):
    print('\n' + ITEM_INFO_HEADER)
    for item in items:
        print_item_row(item)
