import random
from emitter import Emitter

numEmitter = 3
currTime = 0
prevTime = 0
emitters = []

def setup():
    # Environment
    size(1024, 720)
    smooth()
    frameRate(60)
    rectMode(CENTER);

    # Globals
    global currTime, prevTime

    # Variables
    currTime = prevTime = millis()
    margin = 100

    for i in xrange(numEmitter):
        x_pos   = random.randint(margin, width - margin)
        y_pos   = random.randint(margin, height - margin)
        origin  = PVector(x_pos, y_pos)
        emitter = Emitter(origin, getIncrement(0))
        emitters.append(emitter)

    for i in xrange(1000):
        for emitter in emitters:
            emitter.display(getIncrement(i))

def getIncrement(value):
    return value*20;

# def draw():
#     global currTime, prevTime

#     currTime  = millis()
#     deltaTime = (currTime - prevTime) / 1000.0
#     prevTime  = currTime

#     for emitter in emitters:
#         emitter.display(getIncrement(currTime))
  
