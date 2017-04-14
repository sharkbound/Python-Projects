from data.menu import Menu

def say_and_wait(text):
    print(text)
    input('Press any key to go to menu...')


if __name__ == '__main__':
    menu = Menu(['1', '2', '3', '4'], 0, actions=[
        lambda: say_and_wait('item 1 text'),
        lambda: say_and_wait('item 2 text'),
        lambda: say_and_wait('item 3 text'),
        lambda: say_and_wait('item 4 text')])
    menu.main_loop()
