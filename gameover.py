import core
from pygame import Rect

def gameover():

    core.cleanScreen()

    r1 = Rect(275, 300, 230, 100)
    r2 = Rect(275, 500, 230, 100)
    core.Draw.rect((0,145,0), r1)
    core.Draw.rect((255,0,255), r2)
    core.Draw.text((255,0,0), "GAME OVER", (160, 100), 160, "Playbill")
    core.Draw.text((0,0,0), "RETRY", (330, 330), 40, "Bauhaus 93")
    core.Draw.text((0,0,0), "EXIT", (350, 530), 40, "Bauhaus 93")
    if core.getMouseLeftClick():
        if r1.collidepoint(core.getMouseLeftClick()):
            core.memory("Etat", 1)
        if r2.collidepoint(core.getMouseLeftClick()):
            exit()
