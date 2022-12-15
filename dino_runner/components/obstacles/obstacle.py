import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import BIRD, SCREEN_WIDTH


class Obstacle(Sprite):
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, obstacles):
        self.animate()

        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def animate(self):
        if self.image == BIRD:
            if self.index >=30:
                self.index = 0
            if self.index < 15:
                self.obstacle_type = 0
            else:
                self.obstacle_type = 1
            self.index += 1

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))