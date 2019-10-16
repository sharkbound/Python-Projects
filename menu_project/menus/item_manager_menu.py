from data import inv, Item, show_item_table
from menus import Menu
from textadventure.util import ask_int, ask_float


class ItemManagerMenu(Menu):
    def show_command_options(self):
        print('''
1) view items
2) add item
3) remove item
4) modify item

0) go back''')

    def do_1(self, cmd, *args):
        show_item_table(*inv)
        self.pause()

    def do_2(self, cmd, *args):
        name = input('enter the item name: ').strip()
        if not name:
            print('name cannot be empty')
            self.pause()
            return

        elif name in inv:
            print(f'{name} is already in stock, modify it instead')
            self.pause()
            return

        brand = input('enter the item brand (can be empty): ').strip()
        quantity = ask_int('enter the quantity: ', min_=0)
        price = ask_float('enter the price: $', min_=0)

        inv.add(Item(name, quantity, price, brand))

    def do_3(self, cmd, *args):
        show_item_table(*inv)
        name = input('\nenter the name of the item to remove: ')

        if name not in inv:
            print(f'{name} is not in stock')
            return

        inv.remove(name)
        print(f'removed {name}')
        self.pause()

    def do_4(self, cmd, *args):
        show_item_table(*inv)

        name = input('\nenter the item you want to modify: ')
        if name not in inv:
            print(f'{name} is not in stock')
            self.pause()
            return

        item = inv[name]
        action = {'1': 'name', '2': 'brand', '3': 'quantity', '4': 'price'}.get(
            input('what do you want to modify?\n1) name\n2) brand\n3) quantity\n4) price\n>>> '))

        if action == 'name':
            newname = input(f'\nenter new name for "{name}": ').strip()

            if not newname:
                print('name cannot be empty')
                return

            item.name = newname

        elif action == 'brand':
            item.brand = input(f'enter new brand for "{name}" (can be empty): ').strip()

        elif action == 'quantity':
            item.quantity = ask_int(f'enter new quantity for "{name}": ', min_=0)

        elif action == 'price':
            item.price = ask_int(f'enter the new price for "{name}": ', min_=0)
