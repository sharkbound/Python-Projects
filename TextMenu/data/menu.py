import os, sys
from msvcrt import getch

k_arrow_down = 80
k_arrow_up = 72
k_enter = 13


class Menu:
    def __init__(self, options, start_index, actions=None, selected_prefix='--> '):
        self.start_index = start_index
        self.current_index = start_index
        self.options = options
        self.options_count = len(options)
        self.actions = actions
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
            elif key == k_enter:
                self.actions[self.current_index]()

            # self.render()

    def render(self):
        output = ''
        for i, option in enumerate(self.options):
            if i == self.current_index:
                output += self.selected_prefix + str(option)
            else:
                output += str(option)
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
