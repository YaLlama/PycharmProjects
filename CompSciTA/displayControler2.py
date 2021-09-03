class display:

    def __init__(self, dis, width, height):
        global display, screen, displayWidth, displayHeight

        displayWidth = width
        displayHeight = height
        display = dis
        display.set_caption('Window')
        screen = display.set_mode((width, height))
        screen.fill((255, 255, 255))
        display.flip()

    def update(self):
        display.update()
        screen.fill((255, 255, 255))

    def constructLines(self, points):

        lines = []

        for i in range(len(points) - 1):

            if points[i][0] == points[i + 1][0]:
                lines.append([points[i][1], points[i + 1][1], points[i][0], points[i + 1][0], -1])
            else:
                if points[i][0] < points[i + 1][0]:
                    point1 = points[i]
                    point2 = points[i + 1]
                else:
                    point2 = points[i]
                    point1 = points[i + 1]

                # y1, (y1-y2)/(x1-x2), x1, x2
                lines.append([point1[1], (point1[1] - point2[1]) / (point1[0] - point2[0]), point1[0], point2[0]])

        if points[len(points) - 1][0] == points[0][0]:
            lines.append([points[len(points) - 1][1], points[0][1], points[len(points) - 1][0], points[0][0], -1])
        else:
            if points[len(points) - 1][0] < points[0][0]:
                point1 = points[len(points) - 1]
                point2 = points[0]
            else:
                point2 = points[len(points) - 1]
                point1 = points[0]

            # y1, (y1-y2)/(x1-x2), x1, x2
            lines.append([point1[1], (point1[1] - point2[1]) / (point1[0] - point2[0]), point1[0], point2[0]])

        return lines


    def drawShape(self, points, color):
        # get lines for shape
        lines = self.constructLines(points)

        for x in range(displayWidth):

            yBounds = []

            for point in points:
                if point[0] == x:
                    yBounds.append(point[1])

            for line in lines:
                if line[2] <= x <= line[3]:
                    # when the line is vertical and no slope, x1 and x2 match
                    if len(line) == 5:
                        yBounds.append(line[0])
                        yBounds.append(line[1])
                    else:
                        # y − y1 = m(x − x1)
                        # 0   1   2   3
                        # y1, m, x1, x2
                        yBounds.append(int(line[1]*(x - line[2]) + line[0]))

            if len(yBounds) % 2 == 1:
                yBounds = removeDuplicates(yBounds)

            yBounds.sort()

            for i in range(int(len(yBounds)/2)):
                i = i * 2 + 1
                for y in range(yBounds[i] - yBounds[i-1]):
                    screen.set_at((x, y + yBounds[i-1]), color)


def removeDuplicates(list):
    final_list = []
    for num in list:
        if num not in final_list and num+1 not in final_list and num-1 not in final_list:
            final_list.append(num)
    return final_list


# prints list[[],[],[]],[[],[],[]]
def displayList(List):
    for list2 in List:
        print("[", end='')
        print(*list2, sep=", ", end='')
        print("]")
    print("\n")
