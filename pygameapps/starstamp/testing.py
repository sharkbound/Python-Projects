from games.pygame.pygameutil import *

setup()

block_size = 100

for x in range(0, get_width(), block_size):
    for y in range(0, get_height(), block_size):
        draw_rect((0, 100, 0), *snap_to_grid((x, y), block_size), block_size, block_size, 1)

while True:
    for e in get_events():
        check_quit(e)

    if mouse_button_held(2):
        x, y = snap_to_grid(get_mouse_pos(), block_size)
        draw_rect(random_color(), x, y, block_size, block_size)

    update()
