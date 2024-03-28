import pygame
from game_window import *

class Square(pygame.sprite.Sprite):
    def __init__(self, name = "None", width = 50, length = 50):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.width = width
        self.length = length
        self.__x_location = Window.SCREEN_WIDTH / 2 - self.width / 2
        self.__y_location = Window.SCREEN_HEIGHT / 2 - self.length / 2
        self.rbg = (100, 55, 55)
        self.speed = 3
        self.sprint = self.speed + 2
        self.pawn = self.get_object_details()
        self.print_my_object()

    def print_my_object(self):
        print(f"This is my Square {self.name}")

    def get_object_details(self):
        return pygame.Rect((self.__x_location, self.__y_location, self.width, self.length))
    
    def instancate_object(self):
        return pygame.draw.rect(Window.screen, self.rbg, self.pawn)
    
    def move_character(self):
        key = pygame.key.get_pressed()
        movements = {
            pygame.K_a: (-self.sprint if key[pygame.K_LSHIFT] else -self.speed, 0),
            pygame.K_d: (self.sprint if key[pygame.K_LSHIFT] else self.speed, 0),
            pygame.K_w: (0, -self.sprint if key[pygame.K_LSHIFT] else -self.speed),
            pygame.K_s: (0, self.sprint if key[pygame.K_LSHIFT] else self.speed)
        }
        
        for k, v in movements.items():
            if key[k]:
                self.pawn.move_ip(v)