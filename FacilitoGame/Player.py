import pygame

from .Config import (get_width,
                    get_color_player,
                    get_width_player,
                    get_heigth_player,
                    get_speed_player)

from .Sprite import Sprite



class Player(Sprite):

    def __init__(self, display, pos_x=0, pos_y=0):
        Sprite.__init__(self, display, pos_x, pos_y,
                        get_width_player(),
                        get_heigth_player(),
                        get_color_player())

        self.default_position_y = pos_y
        self.speed = get_speed_player()
        self.is_jump = False
        self.is_fall = True

        self.__masss = 2

    def jump(self):
        self.is_jump = True

    def in_default_position(self):
        return self.pos_y >= self.default_position_y

    def update(self):
        if self.is_jump:
            if self.speed >= 0:
                F = ( 0.5 * self.__masss * (self.speed * self.speed) )
            else:
                F = - ( 0.5 * self.__masss * (self.speed * self.speed) )

            self.pos_y = self.pos_y - F
            self.speed = self.speed - 1

            if self.in_default_position():
                self.pos_y = self.default_position_y
                self.is_jump = False
                self.speed = get_speed_player()
