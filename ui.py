from player import Player
from settings import *
import pygame, random
from PIL import Image
from tkinter import Label

class UI:
    def __init__(self, player):
        self.root = None
        self.player = player
        self.display_surface = pygame.display.get_surface()
        try:
            self.font, self.bet_font = pygame.font.Font(UI_FONT, UI_FONT_SIZE), pygame.font.Font(UI_FONT, UI_FONT_SIZE)
            self.win_font = pygame.font.Font(UI_FONT, WIN_FONT_SIZE)
            self.loss_font = pygame.font.Font(UI_FONT, LOSS_FONT_SIZE)
        except:
            print("Error loading font!")
            print(f"Currently, the UI_FONT variable is set to {UI_FONT}")
            print("Does the file exist?")
            quit()
        self.win_text_angle = random.randint(-4, 4)

        #---------------------------------------------------------------------
        
        #---------------------------------------------------------------------

    def display_info(self):
        player_data = self.player.get_data()

        # Balance and bet size
        balance_surf = self.font.render("Balance: $" + player_data['balance'], True, TEXT_COLOR, None)
        x, y = 20, self.display_surface.get_size()[1] - 50
        balance_rect = balance_surf.get_rect(bottomleft = (x, y))

        free_spins_surf = self.font.render("Free Spins: " + str(player_data['free_spins']), True, TEXT_COLOR, None)
        x, y = 20, self.display_surface.get_size()[1] - 10
        free_spins_rect = free_spins_surf.get_rect(bottomleft=(x, y))

        bet_surf = self.bet_font.render("Bet: $" + player_data['bet_size'], True, TEXT_COLOR, None)
        x, y = self.display_surface.get_size()[0] - 20, self.display_surface.get_size()[1] - 50
        bet_rect = bet_surf.get_rect(bottomright = (x, y))

        level_surf = self.font.render("Lygis: " + str(self.player.determine_level()), True, TEXT_COLOR, None)
        x, y = self.display_surface.get_size()[0] - 20, self.display_surface.get_size()[1] - 10
        level_rect = level_surf.get_rect(bottomright=(x, y))

        if float(player_data['music_volume']) < 100:
            volume_surf = self.font.render("Volume: " + str(int(float(player_data['music_volume']))), True, TEXT_COLOR, None)
            x, y = 175, self.display_surface.get_size()[1] - 80
            volume_rect = volume_surf.get_rect(bottomright = (x, y))
        else:
            volume_surf = self.font.render("Volume: " + str(int(float(player_data['music_volume']))), True, TEXT_COLOR, None)
            x, y = 190, self.display_surface.get_size()[1] - 80
            volume_rect = volume_surf.get_rect(bottomright = (x, y))
        
        # Draw player data
        pygame.draw.rect(self.display_surface, False, balance_rect)
        pygame.draw.rect(self.display_surface, False, free_spins_rect)
        pygame.draw.rect(self.display_surface, False, bet_rect)
        pygame.draw.rect(self.display_surface, False, level_rect)
        pygame.draw.rect(self.display_surface, False, volume_rect)
        self.display_surface.blit(balance_surf, balance_rect)
        self.display_surface.blit(free_spins_surf, free_spins_rect)
        self.display_surface.blit(bet_surf, bet_rect)
        self.display_surface.blit(level_surf, level_rect)
        self.display_surface.blit(volume_surf, volume_rect)

        # Print last win if applicable
        if self.player.last_payout:
            last_payout = player_data['last_payout']
            win_surf = self.win_font.render("WIN! $" + last_payout, True, TEXT_COLOR, None)
            x1 = 800
            y1 = self.display_surface.get_size()[1] - 60
            win_surf = pygame.transform.rotate(win_surf, self.win_text_angle)
            win_rect = win_surf.get_rect(center = (x1, y1))
            self.display_surface.blit(win_surf, win_rect)


        if self.player.last_loss and not self.player.last_payout: 
            last_loss = player_data['last_loss']
            loss_surf = self.loss_font.render("Lost :( $" + last_loss, True, TEXT_COLOR, None)
            x1 = 800
            y1 = self.display_surface.get_size()[1] - 60
            #loss_surf = pygame.transform.rotate(loss_surf, self.win_text_angle)
            loss_rect = loss_surf.get_rect(center = (x1, y1))
            self.display_surface.blit(loss_surf, loss_rect)

    def update(self):
        pygame.draw.rect(self.display_surface, 'Black', pygame.Rect(0, 900, 1600, 200))
        self.display_info()

    def win(self):
        start_time = pygame.time.get_ticks()
        display_time = 1500  # in milliseconds
        display_image = True
        self.effect1 = pygame.image.load('graphics/effects/big_win.png').convert_alpha()

        while display_image:
            # check if it's time to stop displaying the image
            current_time = pygame.time.get_ticks()
            if current_time - start_time >= display_time:
                display_image = False

            # display the image if the flag is True
            if display_image:
                self.display_surface.blit(self.effect1, (300, 30))
                pygame.display.flip()