from beam import Beam

numBeams = 5
beamStep = 1
currTime = 0
prevTime = 0
beams    = []

def setup():
    # Environment
    size(1024, 720)
    smooth()
    frameRate(60)
    rectMode(CENTER);

    # Globals
    global beams, currTime, prevTime

    # Variables
    center = PVector(width/2, height/2)
    angleOffset = 360/numBeams
    
    currTime = prevTime = millis()

    for i in xrange(numBeams):
        beams.append(Beam(center, angleOffset * i, beamStep))

def draw():
    ### background(0)
    global currTime, prevTime

    currTime  = millis()
    deltaTime = (currTime - prevTime) / 1000.0
    prevTime  = currTime

    ### ellipse(mouseX, mouseY, 80, 80)

    for i, beam in enumerate(beams):
        # New position
        #pos = PVector(center.x + currTime/25, center.y - currTime/25)

        beam.display(currTime)

        # Noise
        ### noiseX = noise(pos.y * 0.01)*2 + noise(pos.y * 0.1)*0.5

        # ----
        ### noiseX = 1 + currTime/1000
        ### print("noiseX[" + str(i) + "]: " + str(noiseX))
        # ----

