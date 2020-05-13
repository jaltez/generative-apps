import random

def setup():
    numItems   = 20
    numLayers  = 30
    firstLayer = 50
    layerDist  = 10
    layerInc   = 5
    numColors  = 3 #min=2
    lineSkipFactor = 0.25
    
    layerJumpFactor    = 0.9
    gradientJumpFactor = 0.9

    size(1600, 900)
    background(30, 30, 50)

    colors = []
    for i in xrange(numColors):
        c = color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        colors.append(c)

    colorIndex = 0
    colorCount = 0
    colorStep  = float(numLayers) / len(colors)

    lineStack = []
    lineOrigins = [0, 10, 19]
    lineStack = [[] for i in lineOrigins]
    lineItem = random.randint(0, numItems-1)

    center  = PVector(width/2, height/2)
    for i in xrange(numLayers):
        # Gradient color nodes
        colorCount += 1
        if colorCount > colorStep:
            colorCount = 0
            colorIndex += 1

        # Layer alpha
        layerAlpha = int(lerp(0, 255, 1-(i+1.0)/numLayers))
        
        # Angles
        angleStep = 360.0 / numItems
        angleOffset = random.randint(0, 25)

        # Items
        ii = i+1.0
        for j in xrange(numItems):
            # Randoms
            layerJump    = 5 if random.uniform(0, 1) > layerJumpFactor else 0
            gradientJump = 1 if random.uniform(0, 1) > gradientJumpFactor else 0
            randAlpha    = random.randint(0, ii*2)

            # Color calculation
            amt = ii / (numLayers + layerJump) # Inverse of layers + extra random
            c = lerpColor(colors[colorIndex-1+gradientJump], colors[colorIndex], amt)
            c = (c & 0xffffff) | (layerAlpha+randAlpha << 24) # Left bit shifting for changing alpha            

            # Position
            pos = PVector.fromAngle(radians(angleStep * j + angleOffset)) * (firstLayer + (layerDist * pow(ii, 1.25)))
            pos += center

            # Draw
            stroke(c)
            fill(c)
            ellipseSize = i*0.5 + noise(i, j)*15
            ellipse(pos.x, pos.y, ellipseSize, ellipseSize)

            # Radial lines
            if random.uniform(0, 1) > lineSkipFactor:
                for idx, orig in enumerate(lineOrigins):
                    if j == orig:
                        lineStack[idx].append(pos)
                        fill(255, 255, 255);
                        text(j, pos.x-3, pos.y+3)

        numItems += layerInc

    for linePositions in lineStack:
        if len(linePositions) > 1:
            for i in xrange(1, len(linePositions)):
                prev = linePositions[i-1]
                curr = linePositions[i]
                stroke(255);
                line(prev.x, prev.y, curr.x, curr.y)
            
    
def draw():
    pass
