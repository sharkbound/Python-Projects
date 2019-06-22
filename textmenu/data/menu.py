import os, sys
from msvcrt import getch

k_arrow_down = 80
k_arrow_up = 72
k_enter = 13
k_space = 32

class MenuItem:
    def __init__(self, text, onselect):
        self.text = text
        self.on_select = onselect

class Menu:
    def __init__(self, options, selected_prefix='--> '):
        self.current_index = 0
        self.options = options
        self.options_count = len(options)
        self.selected_prefix = selected_prefix

    @staticmethod
    def clear_screen():
        os.system('cls')

    def main_loop(self):
        while True:
            self.render()

            key = ord(getch())
            if key == k_arrow_up:
                self.next_option('up')
            elif key == k_arrow_down:
                self.next_option('down')
            elif key == k_enter or key == k_space:
                self.clear_screen()
                self.options[self.current_index].on_select()
                print('Press any name to return to the menu...')
                getch()

            # self.render()

    def render(self):
        output = ''
        for i, option in enumerate(self.options):
            if i == self.current_index:
                output += self.selected_prefix + option.text
            else:
                output += option.text
            output += '\n'

        # print('\n'*5)
        self.clear_screen()
        print(output)

    def next_option(self, direction):
        new_i = self.current_index + 1 if direction == 'down' else self.current_index - 1

        if new_i < 0:
            new_i = self.options_count - 1
        elif new_i > self.options_count - 1:
            new_i = 0

        self.current_index = new_i
