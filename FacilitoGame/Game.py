import pygame
import sys

from .Config import (get_mode,
                    get_background_color,
                    get_caption,
                    get_fps,
                    get_heigth,
                    get_width,
                    get_floor_color)
from .Player import Player
from .Rect import Rect

class Game:
    def __init__(self):
        pygame.init()

        self.display = self.generate_display()
        self.floor = self.generate_floor()

        self.clock = pygame.time.Clock()
        self.player = Player(self.display)
        self.fps = get_fps()


    def generate_display(self):
        display = pygame.display.set_mode( get_mode() )
        pygame.display.set_caption( get_caption() )
        return display

    def generate_floor(self):
        height = 20
        return Rect(self.display, 0, get_heigth() - height, get_width(), height, (73,48,24))

    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.move_left()
                    if event.key == pygame.K_RIGHT:
                        self.player.move_right()

            self.display.fill( get_background_color() )

            self.player.draw(), self.floor.draw()
            self.player.jump()

            pygame.display.update()
            self.clock.tick(self.fps)
