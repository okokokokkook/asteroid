from menu import menu
from pygame.math import Vector2
import time
import core
from play2 import play2
from pygame import Rect
import random
from gameover import gameover

def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [800, 800]
    core.memory("Etat", 0)
    core.memory("position", Vector2(400, 400))
    core.memory("vitesse", Vector2(0, -1))
    core.memory("projectile", [])
    core.memory("asteroid", Rect(random.randint(50, 700), random.randint(50, 700), 40, 40))
    core.memory("score", 0)
    print("Setup END-----------")


def run():

    if core.memory("Etat") == 0:
        menu()
    if core.memory("Etat") == 1:
        play2()
    if core.memory("Etat") == 2:
        gameover()



core.main(setup, run)
