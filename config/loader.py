from os.path import join
import random

THIEF_POSITION = [
    (220,172), (320,172), (418,172), (515,172),
    (220,300), (320,300), (418,300), (515,300),
    (220,422), (320,422), (418,422), (515,422),
    (220,550), (320,550), (418,550), (515,550)
]
INTRO_PATHS = {
    "begin_image": join('resources', 'images', 'intro', 'begin5.png'),
    "begin_image_red": join('resources', 'images', 'intro', 'begin6.png')
}

def THIEF_PATH(path=None):
    if path is None:
        path = "thief" + str(random.randint(1,8)) + '.png'
    return join('resources', 'images', 'thief', path)
GUN_PATH = join('resources', 'images', 'gun', 'gun.png')
CROSSHAIR_PATH = join('resources', 'images', 'gun', 'crosshair.png')
EXPLOSION_PATH = [join('resources', 'images', 'gun', 'explode', f'tile{str(i).zfill(3)}.png') for i in range(64)]

BACKGROUND_PATH = join('resources', 'images', 'background', 'apartment.jpg')
MUSIC_PATH = join('resources', 'audios', 'main.mp3')
CLICK_PATH = join('resources', 'audios', 'game','click.mp3')
SHOOT_PATH = join('resources', 'audios', 'game','shoot.mp3')

SCORE_PATH = join('resources', 'score.txt')
