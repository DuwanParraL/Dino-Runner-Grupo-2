import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()




while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    if is_daytime == :
        screen.fill((255, 255, 255))  
    else:
        screen.fill((0, 0, 0))  
    pygame.display.flip()  

   
    clock.tick(60)