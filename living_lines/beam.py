import random

class Beam:

    def __init__(self, origin, increment, angle, step, size):
        self.origin   = origin
        self.angle    = angle
        self.step     = step
        self.size     = size
        self.currStep = 0

        self.seed     = random.uniform(1, 100)
        self.offset   = PVector(self.getNoise(increment), 0)
        
        self.color_ini = color(random.randint(50, 150), random.randint(0, 50), random.randint(0, 50))
        self.color_end = color(random.randint(50, 150), random.randint(50, 150), random.randint(50, 150))

    def getNoise(self, value):
        ### origin = PVector(center.x + currTime/25, center.y - currTime/25)
        ### noiseX = noise(origin.y * 0.01)*2 + noise(origin.y * 0.1)*0.5
        return noise( self.seed + value * 0.001 ) * 100

    def display(self, increment):

        noise = self.getNoise(increment);

        pushMatrix()
        translate(self.origin.x, self.origin.y)
        rotate(radians(self.angle))
        translate(-self.offset.x, -self.offset.y)

        # Origin line
        # clr = color(250, 100, 100)
        # stroke(clr)
        # fill(clr)
        # ellipse(0, - self.currStep, 2, 2)

        # Beam
        clr = lerpColor(self.color_ini, self.color_end, norm(self.currStep, 0, self.origin.y))
        stroke(clr)
        fill(clr)
        ellipse(noise, - self.currStep, self.currStep * self.size/100, self.currStep * self.size/100)

        popMatrix()

        self.currStep += self.step
