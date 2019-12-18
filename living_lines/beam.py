import random

class Beam:

    def __init__(self, origin, angle, step=0):
        self.origin   = origin
        self.step     = step
        self.angle    = angle
        self.currStep = 0

        self.seed     = random.uniform(1, 100)
        self.offset   = PVector(self.getNoise(millis()), 0)

        print("seed=" + str(self.seed))

    def getNoise(self, value):
        ### origin = PVector(center.x + currTime/25, center.y - currTime/25)
        ### noiseX = noise(origin.y * 0.01)*2 + noise(origin.y * 0.1)*0.5
        return noise( self.seed + value * 0.001 ) * 100

    def display(self, value):
        
        # Gradient color
        """
        clr1 = color(150, 150, 50)
        clr2 = color(255, 0, 0)
        clr = lerpColor(clr1, clr2, norm(origin.y, 0, center.y))
        stroke(clr)
        fill(clr)

        ellipse(center.x + 150 - i*150 + noise*100, origin.y, 5, 5)
        """

        noise = self.getNoise(value);
        
        print("value=" + str(value))
        print("noise=" + str(noise))

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
        clr1 = color(150, 0, 0)
        clr2 = color(150, 150, 50)
        clr = lerpColor(clr1, clr2, norm(self.currStep, 0, self.origin.y))
        stroke(clr)
        fill(clr)
        ellipse(noise, - self.currStep, self.currStep*0.35, self.currStep*0.35)

        popMatrix()

        self.currStep += self.step
