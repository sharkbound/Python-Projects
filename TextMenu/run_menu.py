from data.menu import Menu, MenuItem


def say_and_wait(text):
    print(text)


if __name__ == '__main__':
    menu = Menu(options=[
        MenuItem('say 1', lambda: say_and_wait('item 1 text')),
        MenuItem('say 2', lambda: say_and_wait('item 2 text')),
        MenuItem('say 3', lambda: say_and_wait('item 3 text')),
        MenuItem('say 4', lambda: say_and_wait('item 4 text'))])

    menu.main_loop()
