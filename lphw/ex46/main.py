from sys import exit
from random import randint
from textwrap import dedent
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
