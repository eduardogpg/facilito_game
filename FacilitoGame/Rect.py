from .Sprite import Sprite

class Rect(Sprite):
    def __init__(self, display, pos_x, pos_y, width, height, color):
        Sprite.__init__(self, display, pos_x, pos_y, width, height, color)
        
