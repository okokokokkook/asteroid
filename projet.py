import menu
from pygame.math import Vector2
import time
import core
import play
import gameover

def setup():
    print("Setup START---------")
    core.fps = 30

    core.WINDOW_SIZE = [800, 800]

    core.memory("position", Vector2(400, 400))
    core.memory("vitesse", Vector2(-1,0))

    core.memory("Etat",0)
    print("Setup END-----------")

def run() :

    print("running")

    if core.memory("Etat") == 0:
        menu()
    if core.memory("Etat") == 1:
        play()
    if core.memory("Etat") == 2:
        gameover()
    #DEPLACEMENT
    core.memory("position",core.memory("position")+ core.memory("vitesse"))

    for proj in core.memory("projectiles") :
        proj["position"]= proj["position"]+proj["vitesse"]

    #DESSIN
    for proj in core.memory("projectiles"):
        core.Draw.circle(proj["cpouleur"], proj["position"],proj["rayon"])

    core.Draw.rect((255,0,0),core.memory("target"))
    core.Draw.text((255,255,255),"Points:",+str(core.memory("points")),20,20)

    #CONTROLES
    if core.getKeyPressList("z") :
        core.memory("vitesse").scale_to_lenth(core.memory("vitesse").lenth()+1)
    if core.getKeyPressList("d") :
        core.memory("vitesse", core.memory("vitesse").rotate(5))
    if core.getKeyPressList("q") :
        core.memory("vitesse",core.memory("vitesse").rotate(-5))

    if core.getKeyPressList("space"):
        if len(core.memory("projectiles")) > 0 :
            if time.time()-core.memory("projectiles")[-1]["startTime"] > 0.5:
                creationTir()
            else:
                creationTir()
core.main(setup(),run())