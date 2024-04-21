import random
import pygame
from constants import RED, GRID_WIDTH, GRIDSIZE, GRID_HEIGHT, WHITE


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRIDSIZE, random.randint(0, GRID_HEIGHT - 1) * GRIDSIZE)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (GRIDSIZE, GRIDSIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, WHITE, r, 1)
