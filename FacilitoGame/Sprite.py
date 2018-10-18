import pygame

class Sprite:
    def __init__(self, display, pos_x, pos_y, width, height, color):
        self.display = display
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        return pygame.draw.rect(
            self.display,
            self.color,
            (self.pos_x, self.pos_y, self.width, self.height)
        )
