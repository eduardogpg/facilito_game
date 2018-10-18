__game = {
    'width' : 800,
    'heigth' : 500,
    'background_color': (10, 10, 10),
    'get_caption': 'Facilito game',
    'floor_color': (73,48,24),
    'fps' : 30
}

__player = {
    'color' : (50, 180, 180),
    'width' : 20,
    'height' : 20,
    'speed' : 10
}

def get_width():
    return __game.get('width')

def get_heigth():
    return __game.get('heigth')

def get_mode():
    return (get_width(), get_heigth())

def get_background_color():
    return __game.get('background_color')

def get_caption():
    return __game.get('get_caption')

def get_fps():
    return __game.get('fps')

def get_color_player():
    return __player.get('color')

def get_width_player():
    return __player.get('width')

def get_heigth_player():
    return __player.get('height')

def get_speed_player():
    return __player.get('speed')

def get_floor_color():
    return __game.get('floor_color')

def get_heigth_floor():
    return 20

def get_pos_y_floor():
    return get_heigth() - get_heigth_floor()
