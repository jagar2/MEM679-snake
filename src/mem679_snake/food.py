import random
import pygame
from config import BLOCK_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, RED


class Food:
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        x = random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        return (x, y)

    def respawn(self):
        self.position = self.random_position()

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            RED,
            pygame.Rect(self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE),
        )
