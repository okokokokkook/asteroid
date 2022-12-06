from menu import menu
from pygame.math import Vector2
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
    core.memory("asteroid", [])
    core.memory("vasteroid", Vector2(random.randint(0, 10), random.randint(0, 10)))
    core.memory("pasteroid", Vector2(random.randint(50, 700), random.randint(50, 700)))
    core.memory("score", 0)
    core.memory("texture1", core.Texture("./BackgroundPlay.jpg", Vector2(0, 0), scaleSize=(800, 800)))
    core.memory("texture2", core.Texture("./Background.webp", Vector2(0, 0), scaleSize=(800, 800)))
    core.memory("vies", 3)
    core.memory("nbasteroids", 0)
    print("Setup END-----------")


def run():
    core.cleanScreen()
    if not core.memory("texture2").ready:
        core.memory("texture2").load()

    core.memory("texture2").show()
    if core.memory("Etat") == 0:
        menu()
    if core.memory("Etat") == 1:
        play2()
    if core.memory("Etat") == 2:
        gameover()

core.main(setup, run)
