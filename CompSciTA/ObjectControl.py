import math

class objectControl:

    def __init__(self, d, w, h):
        global display, width, height

        display = d
        height = h
        width = w

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

    def draw3DShape(self):
        #side is defined as starting at one point and ending at same point, or with an indicator
        pass

    def cube(self, camera):

        points3D = [[-5, 5, 18], [5, 5, 18], [-5, -5, 18], [5, -5, 18], [-5, 5, 23], [5, 5, 23], [-5, -5, 23], [5, -5, 23]]

        face1 = [[5, 5, 18], [-5, 5, 18], [-5, -5, 18], [5, -5, 18]]
        face2 = [[5, 5, 23], [-5, 5, 23], [-5, -5, 23], [5, -5, 23]]
        face3 = [[5, 5, 18], [-5, 5, 18], [-5, 5, 23], [5, 5, 23]]
        face4 = [[5, -5, 18], [-5, -5, 18], [-5, -5, 23], [5, -5, 23]]
        face5 = [[-5, -5, 18], [-5, 5, 18], [-5, 5, 23], [-5, -5, 23]]
        face6 = [[5, -5, 18], [5, 5, 18], [5, 5, 23], [5, -5, 23]]

        faces = [face1, face2, face3, face4, face5, face6]

        faces2D = []
        faces2DDists = []

        for face in faces:

            face2D = self.EDto2D(face, camera)

            faceDist = face2D[len(face2D)-1]
            face2D.remove(faceDist)

            i = len(faces2D)

            for n in range(len(faces2DDists)):
                #want to be ordered (furthest) largest (closest point) to shortest

                dist = faces2DDists[n]
                if faceDist > dist:
                    i = n

            faces2DDists.insert(i, faceDist)
            faces2D.insert(i, face2D)

        for face in faces2D:
            display.drawShape(face, (0, 0, 230))



    def EDto2D(self, points3D, camera):

        points2D = []
        closestPointdist = 99999999999

        fov = 103
        fov = math.radians(fov)
        yFov = fov * height / width



        for i in range(len(points3D)):

            point = points3D[i]

            xDist = point[0] - camera[0]
            yDist = point[1] - camera[1]
            zDist = point[2] - camera[2]

            y = height * (yFov/2 + math.atan(yDist / zDist)) / yFov
            x = width * (fov/2 + math.atan(xDist / zDist)) / fov

            dist = math.sqrt(yDist * yDist + xDist * xDist + zDist * zDist)

            if dist < closestPointdist:
                closestPointdist = dist

            points2D.append([int(x), int(y)])

        points2D.append(closestPointdist)

        return points2D
