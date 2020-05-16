
class CurveGradient:

    def __init__(self, amplitude=30, fillgap=2.5):
        self.amplitude = amplitude
        self.fillGap   = fillgap

    def draw(self):
        #background(200)
        
        # To efficiently set all the pixels on screen, make the set() 
        # calls on a PImage, then write the result to the screen.
        gradient = createImage(width, height, RGB)
        frequency = 0

        for i in xrange(-75, height + 75):
            # Reset angle to 0, so waves stack properly
            angle = 0
            # Increasing frequency causes more gaps
            frequency += 0.001

            for j in xrange(0, width + 75):
                py = i + sin(radians(angle)) * self.amplitude
                angle += frequency
                r = abs(py - i) * 255 / self.amplitude
                g = 255 - abs(py - i) * 255 / self.amplitude
                b = j * ( 255 / (width + 50))
                c = color(r, g, b)
                # Hack to fill gaps. Raise value of fillGap if you increase frequency

                for filler in xrange(self.fillGap):
                    gradient.set(int(j-filler), int(py)-filler, c)
                    gradient.set(int(j), int(py), c)
                    gradient.set(int(j+filler), int(py)+filler, c)

        # Draw the image to the screen
        #set(0, 0, gradient)
        # Another alternative for drawing to the screen
        image(gradient, 0, 0)
