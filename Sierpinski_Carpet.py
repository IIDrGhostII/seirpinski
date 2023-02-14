from turtle import Screen, Turtle, Vec2D

COLOR_MAP = ['blue', 'red', 'green', 'cyan', 'yellow', 'violet', 'orange']

def drawRectangle(points, color, myTurtle):
    myTurtle.fillcolor(color)

    myTurtle.begin_fill()

    for point in points:
        myTurtle.goto(point)

    myTurtle.goto(points[0])

    myTurtle.end_fill()

def sierpinski(points, degree, myTurtle):

    """ Draw a rectangle based on the 4 points given """

    drawRectangle(points, COLOR_MAP[degree % len(COLOR_MAP)], myTurtle)

    if degree > 0:
        origin = points[0] * (2 / 3)  # vectors multiply by a scalar, but not divide

        points = [point * (1 / 3) for point in points]  # new rectangle is 1/3 size of old rectangle

        width, height = points[2] - points[0]  # vector subtraction

        for y in range(3):
            for x in range(3):
                if x == 1 == y:
                    continue  # leave hole in the center

                offset = origin + Vec2D(width * x, height * y)

                sierpinski([offset + point for point in points], degree - 1, myTurtle)

def main():
    # 4 points of the first rectangle based on [x, y] coordinates
    POINTS = [Vec2D(0, 0), Vec2D(0, 300), Vec2D(300, 300), Vec2D(300, 0)]

    myWin = Screen()
    myWin.tracer(True)

    myTurtle = Turtle()
    myTurtle.speed(0)
    myTurtle.penup()

    degree = 2 # Vary the degree of complexity here
    # first call of the recursive function
    sierpinski(POINTS, degree, myTurtle)

    myTurtle.hideturtle()  # hide turtle cursor after drawing is completed

    myWin.tracer(True)
    myWin.exitonclick()  # Exit program when user click on window

main()