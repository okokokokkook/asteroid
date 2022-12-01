import random
import core
import time

from pygame import Rect
from pygame.math import Vector2


def CreationProjectiles():
    P = Vector2(core.memory("position"))
    V = Vector2(core.memory("vitesse"))
    V.scale_to_length(core.memory("vitesse").length() + 10)
    R = 2
    C = (0, 255, 0)
    St = time.time()
    core.memory("projectile").append({"position": P, "vitesse": V, "rayon": R, "couleur": C, "startTime": St})


def play2():

    core.cleanScreen()


    #VAISSEAU

    p1bis = core.memory("vitesse")
    p1bis.scale_to_length(20)
    p1 = core.memory("position") + p1bis

    p2bis = core.memory("vitesse")
    p2bis.scale_to_length(8)
    p2bis = p2bis.rotate(45)
    p2 = core.memory("position") + p2bis

    p3bis = core.memory("vitesse")
    p3bis.scale_to_length(10)
    p3bis = p3bis.rotate(90)
    p3 = core.memory("position") + p3bis

    p4bis = core.memory("vitesse")
    p4bis.scale_to_length(5)
    p4 = core.memory("position") + p4bis

    p5bis = core.memory("vitesse")
    p5bis.scale_to_length(10)
    p5bis = p5bis.rotate(-90)
    p5 = core.memory("position") + p5bis

    p6bis = core.memory("vitesse")
    p6bis.scale_to_length(8)
    p6bis = p6bis.rotate(-45)
    p6 = core.memory("position") + p6bis

    core.Draw.polygon((255, 0, 100), (p1, p2, p3, p4, p5, p6))

    # CHANGEMENT DE COTE

    Py = (core.memory("position").y)
    Px = (core.memory("position").x)

    if Px < 0:
        core.memory("position", (900, Py))

    if Py < 0:
        core.memory("position", (Px, 900))

    if Py > 900:
        core.memory("position", (Px, 0))

    if Px > 900:
        core.memory("position", (0, Py))

    #CONTRÔLES

    if core.getKeyPressList("z"):
        core.memory("vitesse").scale_to_length(core.memory("vitesse").length() + 4)
    if core.getKeyPressList("s"):
        core.memory("vitesse").scale_to_length(core.memory("vitesse").length() - 2)
    if core.getKeyPressList("d"):
        core.memory("vitesse", core.memory("vitesse").rotate(7))
    if core.getKeyPressList("q"):
        core.memory("vitesse", core.memory("vitesse").rotate(-7))


    #PROJECTILES

    core.memory("position", core.memory("position") + core.memory("vitesse"))
    for proj in core.memory("projectile"):
        proj["position"] = proj["position"] + proj["vitesse"]

    for proj in core.memory("projectile"):
        core.Draw.circle(proj["couleur"], proj["position"], proj["rayon"])

    for proj in core.memory("projectile"):
        if time.time() - proj["startTime"] > 3:
            core.memory("projectile").remove(proj)

    if core.getKeyPressList("SPACE"):
        if len(core.memory("projectile")) > 0:
            if time.time() - core.memory("projectile")[-1]["startTime"] > 0.5:
                CreationProjectiles()
        else:
            CreationProjectiles()


    #ASTEROIDES

    core.Draw.rect((150, 50, 0), (core.memory("asteroid")))

    #COLISIONS

    for proj in core.memory("projectile"):
        if core.memory("asteroid").collidepoint(proj["position"].x, proj["position"].y):
            core.memory("asteroid", Rect(random.randint(50, 700), random.randint(50, 700), random.randint(30, 70), random.randint(30, 70)))
            core.memory("projectile").remove(proj)
            core.memory("score", core.memory("score") + 1)

    for ast in core.memory("asteroid"):
        if core.memory("asteroid").collidepoint(Px, Py):
            core.memory("asteroid", Rect(random.randint(50, 700), random.randint(50, 700), random.randint(30, 70),random.randint(30, 70)))
            core.memory("Etat", 2)
            core.memory("position", Vector2(400, 400))
            core.memory("vitesse", Vector2(0, -1))

    core.Draw.text((255, 255, 255), "score :" + str(core.memory("score")), (20, 20), 30, "Monotxt")
