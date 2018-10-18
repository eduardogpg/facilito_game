import pygame

from .Config import (get_width_enemy,
                    get_height_enemy,
                    get_speed_enemy,
                    get_color_enemy)

from .Sprite import Sprite

class Enemy(Sprite):

    def __init__(self, display, pos_x=0, pos_y=0):
        Sprite.__init__(self, display, pos_x, pos_y,
                        get_width_enemy(),
                        get_height_enemy(),
                        get_color_enemy())

        self.speed = get_speed_enemy()


    def update(self):
        self.pos_x -= self.speed
        return self.pos_x
