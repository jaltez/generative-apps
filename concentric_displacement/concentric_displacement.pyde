import random


def setup():
    # CIRCUNFERENCIAS CONCÉNTRICAS DE OBJETOS CON RUIDO DE POSICIÓN AL ALEJARSE DEL CENTRO
    # BASADO EN https://image.shutterstock.com/z/stock-vector-big-data-information-vector-concept-abstract-futuristic-background-with-d-visualization-1017906883.jpg

    numItems   = 20
    numLayers  = 20
    firstLayer = 50
    layerDist  = 22
    layerInc   = 5

    size(1024, 720)

    color_ini = color(random.randint(50, 250), random.randint(100, 150), random.randint(100, 150))
    color_end = color(random.randint(50, 250), random.randint(50, 250), random.randint(50, 250))

    center = PVector(width/2, height/2)
    for i in xrange(numLayers):
        angleStep = 360.0 / numItems
        # print("numItems: " + str(numItems))
        # print("angleStep: " + str(angleStep))
        # print("\n")
        angleOffset = random.randint(0, 45)
        for j in xrange(numItems):
            #pos = PVector.fromAngle(radians((angleStep+angleOffset) * j)) * layerDist * (i+1) # >>>>>>>>>>>>>>>> INTERESTING

            pos = PVector.fromAngle(radians(angleStep * j + angleOffset)) * (firstLayer + (layerDist * (i+1)))
            pos += center

            layerJump = 5 if random.uniform(0, 1) > 0.9 else 0
            c = lerpColor(color_ini, color_end, (i+1.0) / (numLayers + layerJump))
            fill(c)
            ellipse(pos.x, pos.y, 10 + i*0.5, 10 + i*0.5)
            
            # fill(0)
            # textSize(10);
            # text(j, pos.x-7, pos.y+5);
            
        numItems += layerInc
    
def draw():
    pass
