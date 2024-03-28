import pygame
from game_window import *

class Square():
    def __init__(self, name = "None", width = 50, length = 50, x_location = 250, 
                 y_location = 250, r = 100, g = 55, b = 55):
        self.name = name
        self.width = width
        self.length = length
        self.__x_location = x_location
        self.__y_location = y_location
        self.__r = r
        self.__g = g
        self.__b = b
        self.speed = 3
        self.sprint = self.speed + 2
        self.pawn = self.get_object_details()
        self.print_my_object()

    def print_my_object(self):
        print(f"This is my Square {self.name}")

    def get_object_details(self):
        return pygame.Rect((self.__x_location, self.__y_location, self.width, self.length))
    
    def instancate_object(self):
        return pygame.draw.rect(Window.screen, (self.__r, self.__g, self.__b), self.pawn)
    
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