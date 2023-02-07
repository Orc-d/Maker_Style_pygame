import pygame
from settings import *

class Menu:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.create_buttons()
        
    def create_buttons(self):
        
        #메뉴 영역 설정
        size = 180
        margin = 6
        topleft = (WINDOW_WIDTH - size - margin, WINDOW_HEIGHT - size - margin)
        self.rect = pygame.Rect(topleft, (size, size) )
        
        #버튼 영역 설정
        generic_button_rect = pygame.Rect(self.rect.topleft,(self.rect.width / 2, self.rect.height / 2))
        button_margin = 5
        self.tile_button_rect = generic_button_rect.copy().inflate(-button_margin,-button_margin)
        #가운데를 중심으로 줄어듬
        self.coin_button_rect = generic_button_rect.move(self.rect.width / 2, 0).inflate(-button_margin,-button_margin)
        #이동하고 복사
        self.enemy_button_rect = generic_button_rect.move(0, self.rect.width / 2).inflate(-button_margin,-button_margin)
        self.palm_button_rect = generic_button_rect.move(self.rect.width / 2, self.rect.width / 2).inflate(-button_margin,-button_margin)
 
        
    def display(self):
        # pygame.draw.rect(self.display_surface,'red',self.rect)
        pygame.draw.rect(self.display_surface,'green',self.tile_button_rect)
        pygame.draw.rect(self.display_surface,'blue',self.coin_button_rect)
        pygame.draw.rect(self.display_surface,'yellow',self.palm_button_rect)
        pygame.draw.rect(self.display_surface,'black',self.enemy_button_rect)