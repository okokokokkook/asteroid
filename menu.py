import core
from pygame import Rect


def menu():
    core.cleanScreen()

    r1 = Rect(275, 300, 230, 100)
    r2 = Rect(275, 500, 230, 100)
    core.Draw.rect((255,145,0), r1)
    core.Draw.rect((255,0,0), r2)
    core.Draw.text((255,0,100), "PROJET ASTEROIDS", (30, 100), 55, "Magneto")
    core.Draw.text((0,0,0), "NEW GAME", (295, 330), 40, "Bauhaus 93")
    core.Draw.text((0,0,0), "EXIT", (350, 530), 40, "Bauhaus 93")
    if core.getMouseLeftClick():
        if r1.collidepoint(core.getMouseLeftClick()):
            core.memory("Etat", 1)
        if r2.collidepoint(core.getMouseLeftClick()):
            exit()
