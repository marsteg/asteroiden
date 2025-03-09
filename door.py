import pygame
import random
from asteroid import Asteroid
from constants import *
from main import *


class Door(pygame.sprite.Sprite):
    def __init__(self):
        self.position = pygame.Vector2(SCREEN_WIDTH-10, SCREEN_HEIGHT/2)
        self.radius = 50
        pygame.sprite.Sprite.__init__(self, self.containers)

    def draw(self, screen):
        screen.fill((10, 255, 10), (0, 0, SCREEN_WIDTH-10, SCREEN_HEIGHT/2))
        #pygame.draw.rect(screen, (10, 255, 10), (0, 0, SCREEN_WIDTH-10, SCREEN_HEIGHT/2), 2)

    containers = []    
