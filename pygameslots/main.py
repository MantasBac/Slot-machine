from machine import Machine
from ui import UI
from player import Player
from settings import *
#from player import Player
import buttons
import ctypes, pygame, sys

# Maintain resolution regardless of Windows scaling settings
ctypes.windll.user32.SetProcessDPIAware()

class Game:
    def __init__(self):
        # General setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Slot Machine')
        self.clock = pygame.time.Clock()
        self.bg_image = pygame.image.load(BG_IMAGE_PATH).convert_alpha()
        self.grid_image = pygame.image.load(GRID_IMAGE_PATH).convert_alpha()
        self.player = Player()
        self.machine = Machine(self.player)
        self.ui = UI(self.player)
        self.delta_time = 0

        # Sound
        pygame.mixer.music.load('audio/track.mp3')
        pygame.mixer.music.play(loops = -1)

    def run(self):
        player_data = self.player.get_data()
        self.start_time = pygame.time.get_ticks()

        img_plus5 = pygame.image.load('graphics/0/symbols/plus5.png').convert_alpha()
        button_plus5 = buttons.Button(1500, 910, img_plus5, 0.1) 
        img_minus5 = pygame.image.load('graphics/0/symbols/minus5.png').convert_alpha()
        button_minus5 = buttons.Button(1450, 910, img_minus5, 0.1) 

        img_plus55 = pygame.image.load('graphics/0/symbols/plus5.png').convert_alpha()
        button_plus55 = buttons.Button(220, 910, img_plus5, 0.1) 
        img_minus55 = pygame.image.load('graphics/0/symbols/minus5.png').convert_alpha()
        button_minus55 = buttons.Button(280, 910, img_minus5, 0.1) 

        while True:
            player_data = self.player.get_data()

            if  button_plus5.draw(self.screen): 
                self.machine.changebetplus()
            if  button_minus5.draw(self.screen): 
                self.machine.changebetminus()

            if  button_plus55.draw(self.screen) and float(player_data['music_volume']) < 100: 
                self.player.chage_music_volume_plus()
            if  button_minus55.draw(self.screen) and float(player_data['music_volume']) > 0: 
                self.player.chage_music_volume_minus()
                
            # Handle quit operation
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Time variables
            self.delta_time = (pygame.time.get_ticks() - self.start_time) / 1000
            self.start_time = pygame.time.get_ticks()

            pygame.display.update()
            self.screen.blit(self.bg_image, (0, 0))
            self.machine.update(self.delta_time)
            self.screen.blit(self.grid_image, (0, 0))
            self.clock.tick(FPS)

            pygame.mixer.music.set_volume(float(player_data['music_volume']) / 100)

if __name__ == '__main__':
    game = Game()
    game.run()