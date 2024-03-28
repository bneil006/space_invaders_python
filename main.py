import pygame
from game_window import *
from draw_objects import *


def main():
    Window()

    #Instancate & Initiate things
    square = Square()

    #Game
    while Window.running:
        #Before event loop
        Window.screen.fill((0, 0, 0)) # Continues to refill screen black to remove trail
        square.instancate_object()
        square.move_character()

        #Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Window.running = False

        Window.clock.tick(60)  # limits FPS to 60
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()