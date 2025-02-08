from config.settings import *
from config.loader import *
from modules.sprites.game import *
from modules.ui.intro import Intro

if __name__ == '__main__':
    game = Game()
    intro = Intro(game)
    intro.run() 