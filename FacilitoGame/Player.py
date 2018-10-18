import pygame

from .Config import (get_color_player, get_width_player, get_heigth_player)

class Player:

    def __init__(self, display, pos_x=0, pos_y=0):
        self.display = display
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = get_color_player()
        self.height = get_width_player()
        self.width = get_heigth_player()
        self.images = None

    def draw(self):
        return pygame.draw.rect(
            self.display,
            self.color,
            (self.pos_x, self.pos_y, self.width, self.height )
        )

    def jump(self):
        self.pos_y -= 10

    def down(self):
        self.pos_y += 20
