from constants import ITEM_INFO_HEADER
from data import MenuAction, inv, show_item_table
from menus import Menu


class MainMenu(Menu):
    def show_command_options(self):
        print('''
1) manage items
2) search items

0) exit''')

    def do_2(self, cmd, *args):
        items = tuple(inv.search(input('enter search query: ')))

        if not items:
            print('no items found')
        else:
            show_item_table(*items)

        self.pause()

    def do_1(self, cmd, *args):
        from menus import ItemManagerMenu
        return ItemManagerMenu()

    def do_0(self, cmd, *args):
        return MenuAction.exit
