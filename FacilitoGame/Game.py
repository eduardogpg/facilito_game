import pygame
import random
import sys

from .Config import (get_mode,
                    get_background_color,
                    get_caption,
                    get_fps,
                    get_heigth,
                    get_width,
                    get_floor_color,
                    get_heigth_floor,
                    get_pos_y_floor)

from .Player import Player
from .Rect import Rect
from .Enemy import Enemy

class Game:
    def __init__(self):
        pygame.init()

        self.display = self.generate_display()
        self.floor = self.generate_floor(self.display)
        self.player = self.generate_player(self.display)

        self.clock = pygame.time.Clock()
        self.fps = get_fps()
        self.enemies = []

    def generate_display(self):
        display = pygame.display.set_mode( get_mode() )
        pygame.display.set_caption( get_caption() )
        return display

    def generate_player(self, display):
        return Player(display, get_width() / 3,
                               get_heigth() - (get_heigth_floor() * 2 ))

    def generate_floor(self, display):
        return Rect(display, 0, get_pos_y_floor(),
                                get_width(),
                                get_heigth_floor(), get_floor_color() )

    def generate_enemy(self, display):
        pos_x = random.randint(get_width(), get_width() + 3000)
        return Enemy(display, pos_x, get_heigth() - (get_heigth_floor() * 3 ))

    def loop(self):

        enemi = self.generate_enemy(self.display)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.jump()

            self.display.fill( get_background_color() )
            self.player.draw(), self.floor.draw(), enemi.draw()

            if len(self.enemies) < 5:
                self.enemies.append(self.generate_enemy(self.display))
                print("siii")

            for enemy in self.enemies:
                enemy.update()
                enemy.draw()

                if(enemy.pos_x < -100):
                    self.enemies.remove(enemy)


            self.player.update()

            pygame.display.update()
            self.clock.tick(self.fps)
