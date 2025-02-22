from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH
from random import randint

class PowerUp(Sprite):
    def __init__(self, image, power_up_type):
        self.type = power_up_type
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + randint(600, 800)
        self.rect.y = randint(125, 200)
        self.start_time = 0
        self.duration = randint(2, 5)

    def update(self, game_speed, power_ups):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            power_ups.pop()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))