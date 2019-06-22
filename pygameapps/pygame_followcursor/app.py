import pygame

from pygame import display, draw  # import them individualy so pycharm intelisence will pick them up

pygame.init()

screen_size = (600, 600)

screen = display.set_mode(screen_size)

close_game = False

pos = (0, 0)

while not close_game:

    # Event handling
    for e in pygame.event.get():

        # Quit event handling
        if e.type == pygame.QUIT:
            pygame.quit()
            break

        # Key press event handling
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                pygame.quit()
                break

        # Mouse moved event handling
        if e.type == pygame.MOUSEMOTION:
            pos = e.pos

    # Clearing screen
    screen.fill((0, 0, 0))

    # Rendering
    # draw.rect(screen, (255, 0 ,0), [pos[0]-5, pos[1]-5, 10, 10])
    draw.circle(screen, (255, 0, 0), pos, 10)

    # Update screen
    display.update()
