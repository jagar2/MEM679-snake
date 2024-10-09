import random
import pygame
from mem679_snake.config import BLOCK_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, RED


class Food:
    """
    A class to represent the food in the snake game.

    Attributes
    ----------
    position : tuple
        The (x, y) coordinates of the food on the game screen.

    Methods
    -------
    random_position():
        Generates a random position for the food within the game boundaries.
    
    get_rect():
        Returns a pygame.Rect object representing the food's position and size.
    
    respawn():
        Respawns the food at a new random position.
    
    draw(screen):
        Draws the food on the given screen.
    """
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        x = random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        return (x, y)

    def get_rect(self):
        x, y = self.position
        return pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)

    def respawn(self):
        self.position = self.random_position()

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            RED,
            pygame.Rect(self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE),
        )
