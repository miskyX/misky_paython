
import pygame

from pygame.sprite import Sprite

#要继承模块pygame.sprite中导入的Sprite类

class Bullet(Sprite):
    '''创建一个对飞船发射子弹，进行管理的类'''

    def __init__(self,ai_settings,screen,ship):

        '''在飞船所在位置创建一个子弹对象'''
        super().__init__()  #super函数继承父类属性，回忆一下
        self.screen = screen

        # 在（0,0）处创建一个宽长的矩形
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        '''向上移动的子弹'''
        self.y = self.y - self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        '''在屏幕上绘制子弹'''
        pygame.draw.rect(self.screen,self.color,self.rect)
