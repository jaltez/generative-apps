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
    background(30, 30, 50)

    color_ini = color(random.randint(150, 250), random.randint(100, 150), random.randint(100, 150))
    color_end = color(random.randint(50, 150), random.randint(50, 150), random.randint(50, 150))

    center = PVector(width/2, height/2)
    for i in xrange(numLayers):
        angleStep = 360.0 / numItems
        # print("numItems: " + str(numItems))
        # print("angleStep: " + str(angleStep))
        # print("\n")
        angleOffset = random.randint(0, 45)
        ii = i+1.0
        for j in xrange(numItems):
            #pos = PVector.fromAngle(radians((angleStep+angleOffset) * j)) * layerDist * ii # >>>>>>>>>>>>>>>> INTERESTING

            pos = PVector.fromAngle(radians(angleStep * j + angleOffset)) * (firstLayer + (layerDist * ii))
            pos += center

            layerJump = 5 if random.uniform(0, 1) > 0.9 else 0
            amt = ii / (numLayers + layerJump) # Inverse of layers + extra random
            c = lerpColor(color_ini, color_end, amt)
            
            stroke(c)
            fill(c)
            ellipseSize = 10 + i*0.5
            ellipse(pos.x, pos.y, ellipseSize, ellipseSize)
            
            # fill(0)
            # textSize(10);
            # text(j, pos.x-7, pos.y+5);
            
        numItems += layerInc
    
def draw():
    pass
