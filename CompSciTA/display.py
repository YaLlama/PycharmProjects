class display:

    # Pygame Variables
    def setUpScreen(self, dis, w, h):
        global display, screen, width, height

        width = w
        height = h
        display = dis
        display.set_caption('Window')
        screen = display.set_mode((w, h))
        screen.fill((255, 255, 255))
        display.flip()

    # Colors
    def setUpColors(self):
        global forestGreen, darkBlue, colorList

        forestGreen = (34, 139, 34)
        darkBlue = (0, 0, 146)
        colorList = [forestGreen, darkBlue]

    def __init__(self, dis, width, height):
        self.setUpScreen(dis, width, height)
        self.setUpColors()

    def changeColor(self, num):

        screen.set_at((100, 100), colorList[num])

    def update(self):
        display.update()
        screen.fill((255, 255, 255))

    # returns point slope form of lines of a shape when given verticies of a shape
    def constructLines(self, points):
        # points is a list of [x,y] coordinates

        # y1, slope, x1, x2
        lineSegments = []

        for i in range(len(points) - 1):
            point1 = points[i]
            point2 = points[i + 1]

            if point1[0] == point2[0]:
                lineSegments.append([point1[1], point2[1], point1[0]])
            else:
                # y1, (y1-y2)/(x1-x2), x1, x2
                lineSegments.append(
                    [point1[1], (point1[1] - point2[1]) / (point1[0] - point2[0]), point1[0], point2[0]])

        point1 = points[len(points) - 1]
        point2 = points[0]
        if point1[0] == point2[0]:
            lineSegments.append([point1[1], point2[1], point1[0]])
        else:
            # y1, (y1-y2)/(x1-x2), x1, x2
            lineSegments.append([point1[1], (point1[1] - point2[1]) / (point1[0] - point2[0]), point1[0], point2[0]])

        return lineSegments

    # prints list [[],[],[]],[[],[],[]]
    def print2Dlist(self, List):
        for list2 in List:
            print("[", end='')
            print(*list2, sep=", ", end='')
            print("]")

        print("\n")

    def drawShape(self, points, color):
        # get lines for shape
        lineSegments = self.constructLines(points)

        # for each row
        for y in range(height):
            # set of x cords
            xs = []

            # for each line
            for lines in lineSegments:
                if len(lines) == 3:
                    if min(lines[0], lines[1]) <= y <= max(lines[0], lines[1]):
                        xs.append(lines[2])
                else:
                    # y-y1 = m(x - x1)

                    # rename variables
                    y1 = lines[0]
                    m = lines[1]
                    x1 = lines[2]
                    x2 = lines[3]

                    # Get the x cord based on the row
                    if (m == 0):
                        xs.append(int(x1))
                        xs.append(int(x2))
                    else:
                        x = int((y - y1) / m + x1)

                        # if its less than the largest point of the linesegment or larger than the smallest
                        if min(x1, x2) <= x <= max(x1, x2):
                            xs.append(x)

            # sort xs smallest to largest
            xs.sort()
            # print(y)
            # print(*xs, sep=", ")
            # print("true")

            for i in range(len(xs)):
                if i % 2 == 1:

                    for x in range(xs[i] - xs[i - 1]):
                        # print((x + xs[i-1]))
                        screen.set_at((x + xs[i - 1], y), color)

            # print()

    def antiAliasing(self, points, color):
        lineSegments = self.constructLines(points)
        for y in range(height):
            for lines in lineSegments:
                # y-y1 = m(x - x1)

                # rename variables
                y1 = lines[0]
                m = lines[1]
                x1 = lines[2]
                x2 = lines[3]

                # Get the x cord based on the row
                x = int((y - y1) / m + x1)

                # if its less than the largest point of the linesegment or larger than the smallest
                if min(x1, x2) <= x <= max(x1, x2):
                    screen.set_at((x, y + 1), color)

    def graph(self, lineSegments, color):
        for lines in lineSegments:
            # y-y1 = m(x - x1)
            y1 = lines[0]
            m = lines[1]
            x1 = lines[2]
            x2 = lines[3]

            if (x1 < x2):
                mx = x1
                Mx = x2
            else:
                mx = x2
                Mx = x1

            for i in range(Mx - mx):
                i += mx
                # ((i, m(i - x1)) + y1)
                screen.set_at((i, int(m * (i - x1) + y1)), color)
