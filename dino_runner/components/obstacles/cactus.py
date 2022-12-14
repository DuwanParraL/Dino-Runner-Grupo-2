from random import randint
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS

class Cactus(Obstacle):
    CACTUS = {
        'LARGE': (LARGE_CACTUS, 300),
        'SMALL': (SMALL_CACTUS, 325),
    }
    
    def __init__(self, cactus_type):
        image,cactus_pos = self.CACTUS[cactus_type]
        cactus_type = randint(0,2)
        super().__init__(image[cactus_type])
        self.rect.y = cactus_pos

    