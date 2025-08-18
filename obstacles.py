
import random

OBSTACLE_COLOR = (128, 0, 128)
OBSTACLE_COUNT = 7


class Obstacles:

    def __init__(self, screen_width, screen_height, snake_block, snake_start, food_pos):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.snake_block = snake_block
        self.snake_start = snake_start
        self.food_pos = food_pos
        self.obstacles = self.generate_obstacles()

    def generate_obstacles(self):
        obstacles = []
        while len(obstacles) < OBSTACLE_COUNT:
            ox = round(
                random.randrange(0, self.screen_width - self.snake_block) / 10.0
            ) * 10.0
            oy = round(
                random.randrange(0, self.screen_height - self.snake_block) / 10.0
            ) * 10.0
            if (
                [ox, oy] == self.snake_start or
                [ox, oy] == self.food_pos or
                [ox, oy] in obstacles
            ):
                continue
            obstacles.append([ox, oy])
        return obstacles

    def draw(self, screen):
        import pygame
        for obs in self.obstacles:
            pygame.draw.rect(
                screen, OBSTACLE_COLOR,
                [obs[0], obs[1], self.snake_block, self.snake_block]
            )

    def is_collision(self, pos):
        return pos in self.obstacles
