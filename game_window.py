import pygame

class Window():
        SCREEN_WIDTH = 640
        SCREEN_HEIGHT = 480
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = pygame.time.Clock()
        running = True