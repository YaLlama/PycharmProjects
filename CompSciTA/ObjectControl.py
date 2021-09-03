import math

class objectControl:

    def __init__(self, disclass):
        global display

        display = disclass

    def regularShape(self, X, Y, radius, sides, color):
        points = []
        frequencyRad = 2* math.pi / sides
        for i in range(sides):
            i += .5
            theta = i * frequencyRad
            y = math.cos(theta) * radius
            x = math.sin(theta) * radius
            points.append([int(x+X), int(y+Y)])

        display.drawShape(points, color)


