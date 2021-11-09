from pygame_util import *

setup((600, 600))

t = Text(font_name='impact', size=100, text='hello!')
b = Button((200, 200), 100, 100, gray)

while running():
    for e in get_events():
        check_quit(e)

    b.draw(red)
    blit(t.render, (200, 200))

    update()
