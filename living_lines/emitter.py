import random
from beam import Beam

class Emitter:
    
    def __init__(self, origin, increment):
        numBeams    = random.randint(3, 8)
        step        = random.uniform(1, 2)
        size        = random.randint(1, 20)
        angleOffset = 360/numBeams

        self.beams = []
        for i in xrange(numBeams):
            beam = Beam(origin, increment, angleOffset * i, step, size)
            self.beams.append(beam)

    def display(self, increment):
        for beam in self.beams:
            beam.display(increment)