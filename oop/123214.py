def get_number_aliens_x(ai_sittings,alien_width):
    '''计算一行能放下多少个外星人，X轴计算宽度'''
    available_space_x = ai_sittings.screen_width - 2 * alien_width  # 计算屏幕可用宽度‘
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x
    GG = number_aliens_x
    print(GG)
get_number_aliens_x()
