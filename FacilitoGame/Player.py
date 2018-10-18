import pygame

from .Config import (get_width,
                    get_color_player,
                    get_width_player,
                    get_heigth_player,
                    get_speed_player)

from .Sprite import Sprite

class Player(Sprite):

    def __init__(self, display, pos_x=750, pos_y=0):
        Sprite.__init__(self, display, pos_x, pos_y,
                        get_width_player(),
                        get_heigth_player(),
                        get_color_player())

        self.speed = get_speed_player()
        self.velocity = 0.5
        self.masss = 0.1
        self.is_jump = True

    def move_left(self):
        if self.pos_x > 0:
            self.pos_x -= self.speed

    def move_right(self):
        if self.pos_x < get_width() - self.width:
            self.pos_x += self.speed

    def jump(self):
        if self.is_jump:

            if self.velocity == 0:
                fall = ( 0.5 * self.masss * (self.velocity * self.velocity) )
            else:
                fall = -( 0.5 * self.masss * (self.velocity * self.velocity) )

            # Change position
            self.pos_y = self.pos_y - fall

            # Change velocity
            self.velocity = self.velocity - 1

            # If ground is reached, reset variables.
            if self.pos_y >= 460:
                print ("Aquí")
                self.pos_y = 460
                self.is_jump = False
                self.velocity = 8
