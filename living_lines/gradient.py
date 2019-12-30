import random

class Gradient:

    def __init__(self):
        pass

    def draw(self):
        # Random pre-sort
        order = [0,1,2]
        random.shuffle(order)

        # Third color
        z_ = random.randint(150, 250)

        # Screen loop
        for y in xrange(height):
            for x in xrange(width):
                # Colors
                x_ = lerp(100, 150, norm(x, 0, height))
                y_ = lerp(150, 250, norm(y, 0, width))

                # Color sorting
                args = [a for i, a in sorted(zip(order,[x_, y_, z_]))]

                # Pixel draw
                stroke(*args)
                point(x, y)
