from os.path import join
import random

THIEF_POSITION = [
    (220,172), (320,172), (418,172), (515,172),
    (220,300), (320,300), (418,300), (515,300),
    (220,422), (320,422), (418,422), (515,422),
    (220,550), (320,550), (418,550), (515,550)
]
INTRO_PATHS = {
    "begin_image": join('resources', 'images', 'intro', 'Begin1.png'),
    "begin_image_red": join('resources', 'images', 'intro', 'Begin3.png')
}

def THIEF_PATH(path=None):
    if path is None:
        path = "thief" + str(random.randint(1,8)) + '.png'
    return join('resources', 'images', 'thief', path)

BACKGROUND_PATH = join('resources', 'images', 'background', 'apartment.jpg')
