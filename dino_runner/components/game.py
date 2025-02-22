import pygame
from dino_runner.utils.constants import (BG,ICON,SCREEN_HEIGHT,SCREEN_WIDTH, TITLE, FPS, FONT_BOLD, DINO_START, RESET, GAME_OVER, SHIELD_TYPE,HEART)
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager 
from dino_runner.components.score import Score
from dino_runner.components.power_ups.power_up_manager import PowerUpManager

from dino_runner.components.heart import Heart


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)

        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.score = Score()
        self.power_up_manager = PowerUpManager()
        self.executing = False
        self.death_counts = 0
        self.half_screen_width = SCREEN_WIDTH // 2
        self.half_screen_height = SCREEN_HEIGHT // 2
        self.heart_manager = Heart()
        self.hearts = 3
        self.soundJump = pygame.mixer.Sound("sound/die.wav")
       

    def execute(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                self.show_menu()
        pygame.quit()

    def run(self):
        self.hearts = 3
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.score.points = 0
        
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self.game_speed, self.player, self.on_death)
        self.power_up_manager.update(self.game_speed, self.score.points, self.player)
        self.score.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 224, 0)) #utilizar para hacer noche
        self.draw_background()
        self.player.draw(self.screen)
        self.player.draw_active_power_up(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.heart_manager.draw(self.screen, self.hearts)
        self.score.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed


    def show_menu(self):
        self.screen.fill((221, 219, 203))
        if self.death_counts == 0:
            self.draw_image(DINO_START, 40, 150)
            self.menu_view('Press any key to start...', 0, -10)
        else:
            self.draw_image(GAME_OVER, 190, 160)

            self.menu_view('Press any key to restart...', 0, -40)
            self.menu_view(f'Your score: {self.score.points}', 0, -90)
            self.menu_view(f'Your deaths: {self.death_counts}', 0, -140)
        pygame.display.update()
        self.handle_menu_event()

    def handle_menu_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.executing = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def menu_view(self, text, x_pos, y_pos):
        font = pygame.font.Font(FONT_BOLD, 30)
        message = font.render(text, True, (0, 0, 0))
        message_rect = message.get_rect()
        message_rect.center = (self.half_screen_width - x_pos, self.half_screen_height - y_pos)
        self.screen.blit(message, message_rect)

    def draw_image(self, image, x_pos, y_pos):
        self.screen.blit(image, (self.half_screen_width - x_pos, self.half_screen_height - y_pos))

    def on_death(self):
        has_shield = self.player.type == SHIELD_TYPE
        if not has_shield:
            if self.hearts > 0:
                self.hearts -= 1
            else:
                self.draw()
                self.hearts 
                self.death_counts += 1
                self.soundJump.play()
                self.playing = False
                
        return not has_shield