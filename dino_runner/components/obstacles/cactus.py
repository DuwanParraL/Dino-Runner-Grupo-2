from random import randint
from dino_runner.components.obstacles.obstacles import Obstacles



class Cactus(Obstacles):
    def __init__(self, imagen):
        cactus_type = randint(0, 2)
        super().__init__(imagen[cactus_type])
        self.rect.y = 325


