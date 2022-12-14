import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS


class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def obstacle_generate(self, obstacle_type):
        if obstacle_type == 0:
            cactus_type = 'SMALL'
            obstacle = Cactus(cactus_type)
        else:
            cactus_type2 = 'LARGE'
            obstacle = Cactus(cactus_type2)

        return obstacle

    def update(self, game):
        if len(self.obstacles) == 0:
            obstacle_type  = random.randint (0,2)
            obstacle = self.obstacle_generate(obstacle_type)
            self.obstacles.append(obstacle)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if obstacle.rect.colliderect(game.player.rect):
                pygame.time.delay(1000)
                game.playing = False
                break
           

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
            