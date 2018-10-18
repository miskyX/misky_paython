
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''创建一个外星人的类'''
    def __init__(self,ai_settings,screen):
        '''初始化外星人并设置其初始位置'''
        super().__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/alien.png')
        self.image = pygame.transform.scale(self.image,(50, 50))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width  #图像的位置位于左上角，位置跟ship类不同，
        self.rect.y =self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        '''外星人向左或向右移动'''
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        '''这里很厉害，因为利用乘上+1或者-1来实现方向的改变'''
        self.rect.x = self.x

    def check_edges(self):
        '''外星人碰到边缘，就返回True'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= screen_rect.left:
            return True

