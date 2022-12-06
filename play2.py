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

def creationasteroid():
    v = core.memory("vasteroid")
    p = core.memory("pasteroid")
    h = Rect(random.randint(50, 700), random.randint(50, 700), 90, 90)
    st = time.time()
    core.memory("asteroid").append({"vitesse": v,"position": p, "startTime": st, "hitbox": h})


def play2():

    core.cleanScreen()

    #FOND

    core.cleanScreen()
    if not core.memory("texture1").ready:
        core.memory("texture1").load()

    core.memory("texture1").show()

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
        core.memory("position", (800, Py))

    if Py < 0:
        core.memory("position", (Px, 800))

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

    for ast in core.memory("asteroid"):
        core.memory("texture3", core.Texture("./Asteroid.png", ast["hitbox"]))
        if not core.memory("texture3").ready:
            core.memory("texture3").load()

        core.memory("texture3").show()
    if len(core.memory("asteroid")) == 0:
        creationasteroid()
    else:
        if time.time() - core.memory("asteroid")[-1]["startTime"] > 2:
            creationasteroid()

    for ast in core.memory("asteroid"):
        if time.time() - ast["startTime"] > 6:
            core.memory("asteroid").remove(ast)

    #COLISIONS

    for ast in core.memory("asteroid"):
        for proj in core.memory("projectile"):
            if ast["hitbox"].collidepoint(proj["position"].x, proj["position"].y):
                core.memory("asteroid").remove(ast)
                core.memory("projectile").remove(proj)
                core.memory("score", core.memory("score") + 1)

    for ast in core.memory("asteroid"):
        if ast["hitbox"].collidepoint(Px, Py):
            core.memory("asteroid").remove(ast)
            core.memory("vies", core.memory("vies") - 1)

    if core.memory('vies') == 0:
        core.memory("position", Vector2(400, 400))
        core.memory("vitesse", Vector2(0, -1))

        core.memory("vies", 3)
        core.memory("Etat", 2)

    core.Draw.text((255, 255, 255), "SCORE :" + str(core.memory("score")), (20, 20), 30, "Monotxt")
    core.Draw.text((255, 255, 255), "VIES :" + str(core.memory("vies")), (20, 60), 30, "Monotxt")