
'''用来存储大量的运行函数'''
import sys

from time import  sleep #内置的，导入模块time中的sleep函数，游戏暂停

import pygame

from bullet import Bullet

from alien import Alien


def check_keydown_events(event,  ai_settings,screen,ship,bullets):
    '''响应键盘被按下'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
        # 如果检测到向右的按键，则moving标志为true, 则rect值+1，即向右移动
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
        #如果检测到空格键，执行下面
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings,screen,ship,bullets):
    '''如果没有达到限制就发射一颗子弹'''
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)  # 产生一个new_bullet
        bullets.add(new_bullet)  # Group合集增加内容

def check_keyup_events(event,ship):
    '''响应键盘被松开'''
    if event.key == pygame.K_RIGHT:  # 如果检测到向右的按键，则rect值
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_play_button_event(ai_settings,screen,stats,scoreboard,play_button,
                            ship,aliens,bullets,mouse_x,mouse_y):
    '''相应按钮被点击事件'''
    if play_button.rect.collidepoint(mouse_x,mouse_y): #X与Y重合，就是被点击
        '''玩家单击play时，才开始游戏'''
        button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
        if button_clicked and not stats.game_active:
            '''如果在非活动状态下点击鼠标，才开始运行下面程序'''
            # 重置游戏设置
            ai_settings.initialize_dynamic_settings()
            # #隐藏光标
            pygame.mouse.set_visible(False)
            #重置统计信息
            stats.reset_stats()
            stats.game_active = True
            #重置记分牌图像
            scoreboard.prep_score()
            scoreboard.prep_level()
            scoreboard.prep_ships()
            #清空外星人和子弹列表
            aliens.empty()
            bullets.empty()
            #创建新的外星人和飞船
            create_fleet(ai_settings,screen,ship,aliens)
            ship.center_ship()


def check_events(ai_settings,screen,stats,scoreboard,play_button,
                 ship,aliens,bullets):
    '''相应按键和鼠标事件'''
    # 监视键盘和鼠标事件
    for event in pygame.event.get():  # even表示事件
        if event.type == pygame.QUIT:  # 如果事件类型为quit，系统退出
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x ,mouse_y = pygame.mouse.get_pos() #鼠标的坐标位置
            check_play_button_event(ai_settings,screen,stats,scoreboard,play_button,
                            ship,aliens,bullets,mouse_x,mouse_y)

        elif event.type == pygame.KEYDOWN:  #如果检测到键盘被按下,
            check_keydown_events(event,ai_settings,screen,ship,bullets)

        elif event.type == pygame.KEYUP:   #如果检测到键盘被弹起
            check_keyup_events(event,ship)


def update_screen(ai_settings,stats,screen,scoreboard,ship,aliens,bullets,play_button):
    '''更新屏幕上的图像，并切换到新屏幕'''
    screen.fill(ai_settings.bg_color)  # 颜色填充屏幕
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    scoreboard.show_score()
    # 让刚绘制的屏幕出现
    #如果游戏处于非活动状态，就绘制按钮，让他开始游戏
    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()  # flip（）方法：重绘图画，平滑更新


def get_number_aliens_x(ai_sittings,alien_width):
    '''计算一行能放下多少个外星人，X轴计算宽度'''
    avilable_space_x = ai_sittings.screen_width - 2 * alien_width
    number_aliens_x = int(avilable_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
    '''计算屏幕能放下多少行，要考虑屏幕总体的高度，减去下面的飞船，要考虑外星人的高度'''
    available_space_y = ai_settings.screen_height - ship_height - (3 * alien_height)
    number_rows = int((available_space_y) / (3 * alien_height))
    return number_rows


def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    '''创建一个外星人，并放在当前行'''
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings,screen,ship,aliens):
    '''创建外星人群（逐行）'''
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)



def check_bullet_alien_collisions(ai_settings,screen,stats,scoreboard,ship,aliens,bullets):
    '''为了优化性能，重构参数，把相应子弹碰撞独立成函数'''
    '''检查是否有子弹打中了敌人，如果有，删除子弹和敌人'''
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    '''#sprite.collide是一种检测重叠的方法，或者碰撞,
    意义是遍历每个子弹，再遍历每个外星人，每当有重叠，就在字典中添加一堆键值
    全部打死后，重新生成，就是看aliens是否为空'''
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            scoreboard.prep_score()
    '''如果全部消灭事件达成，设置新事件'''
    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        stats.level += 1
        scoreboard.prep_level()
        create_fleet(ai_settings,screen, ship, aliens)  # 调用函数，新产生一批外星人

def update_bullets(ai_settings,screen,stats,scoreboard,ship,aliens,bullets):
    '''更新子弹的位置，并删除消失的子弹'''
    # 删除已消失的子弹
    for bullet in bullets.copy():  # 如果满足条件消失，就从编组里面删除
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings,screen,stats,scoreboard,ship,aliens,bullets)
    bullets.update()



def change_fleet_direction(ai_setting,aliens):
    '''实现外星人改变放下，下降'''
    for alien in aliens.sprites():
        alien.rect.y += ai_setting.fleet_drop_speed  #下降一个值
    ai_setting.fleet_direction *= -1 #向左

def check_fleet_edges(ai_sittings,aliens):
    '''外星人到达边缘，采取相应措施'''
    for alien in aliens.sprites():
        if alien.check_edges():  #就是如果碰到边缘
            change_fleet_direction(ai_sittings,aliens) #执行下降并变向一次，后面打断
            break

def ship_hit(ai_settings,stats,screen,scoreboard,ship,aliens,bullets):
    '''相应撞击事件'''
    if stats.ships_left > 0:
        #撞击后，ships_left数量减1
        stats.ships_left -= 1
        #更新飞船信息
        scoreboard.prep_ships()
        #清空外星人和子弹列表
        aliens.empty()
        bullets.empty()
        #创建一群新外星人，新飞船，刷新
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        #暂停游戏
        sleep(0)
    else:
        '''发生了碰撞，游戏状态改为关闭'''
        stats.game_active =False
        pygame.mouse.set_visible(True) #鼠标可见，方便关闭

def check_aliens_bottom(ai_settings,stats,screen,scoreboard,ship,aliens,bullets):
    '''检查飞船是否到达屏幕底部'''
    screen_rect =screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #相当于碰撞了飞船
            ship_hit(ai_settings,stats,screen,scoreboard,ship,aliens,bullets)
            break

def update_aliens(ai_settings,stats,screen,scoreboard,ship,aliens,bullets):
    '''更新外星人位置，并实现碰撞改变方向等'''
    check_fleet_edges(ai_settings,aliens) #调用函数，实现了嵌套
    '''检测飞船与外星人的碰撞，结束游戏'''
    if pygame.sprite.spritecollideany(ship,aliens):
        print("Fuck ! 发生了猛烈撞击！")
        ship_hit(ai_settings,stats,screen,scoreboard,ship,aliens,bullets)
    check_aliens_bottom(ai_settings,stats,screen,scoreboard,ship,aliens,bullets)
    '''检查飞船是否碰到底部，结束游戏'''
    aliens.update()


