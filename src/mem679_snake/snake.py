import pygame
from config import BLOCK_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, GREEN

class Snake:
    def __init__(self):
        self.body = [(100, 50), (90, 50), (80, 50)]
        self.direction = "RIGHT"
        self.new_block = False  # Flag to indicate when to grow the snake

    def get_head_position(self):
        return self.body[0]  # Return the coordinates of the snake's head

    def change_direction(self, new_direction):
        opposite_directions = {
            "UP": "DOWN",
            "DOWN": "UP",
            "LEFT": "RIGHT",
            "RIGHT": "LEFT",
        }
        if new_direction != opposite_directions.get(self.direction):
            self.direction = new_direction

    def move(self):
        x, y = self.get_head_position()

        # Update head position based on the current direction
        if self.direction == "UP":
            y -= BLOCK_SIZE
        elif self.direction == "DOWN":
            y += BLOCK_SIZE
        elif self.direction == "LEFT":
            x -= BLOCK_SIZE
        elif self.direction == "RIGHT":
            x += BLOCK_SIZE

        new_head = (x, y)
        self.body.insert(
            0, new_head
        )  # Insert new head position at the start of the body list

        # Remove last block if no new block is needed
        if not self.new_block:
            self.body.pop()
        else:
            self.new_block = False  # Reset flag after growing

    def grow(self):
        self.new_block = True  # Set flag to grow on the next move

    def check_collision_with_self(self):
        return self.get_head_position() in self.body[1:]

    def check_collision_with_walls(self):
        x, y = self.get_head_position()
        return x < 0 or x >= SCREEN_WIDTH or y < 0 or y >= SCREEN_HEIGHT

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(
                screen,
                GREEN,
                pygame.Rect(segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE),
            )
