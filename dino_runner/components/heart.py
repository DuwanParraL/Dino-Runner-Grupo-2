import pygame


from dino_runner.utils.constants import HEART

class Heart():
    def __init__(self):
        self.image = HEART
        self.image_rect = self.image.get_rect()#pintamos la imagen
        self.image_rect.y = 20
        self.image_rect.x = 20
        
        
    def draw(self,screen,live):
        separeishon = 0  #variable
        for i in range(0,live):     #multiplica
            screen.blit(self.image, (self.image_rect.x + separeishon, self.image_rect.y))
            separeishon += 30   #separación