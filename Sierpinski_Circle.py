import turtle
import math

def drawCircle(point, radius, color, myTurtle):
    myTurtle.up()
    myTurtle.goto(point)
    myTurtle.down()
    myTurtle.fillcolor(color)
    myTurtle.begin_fill()
    myTurtle.circle(radius)
    myTurtle.end_fill()

def sierpinskiCircle(point, radius, degree, color, myTurtle):
    drawCircle(point, radius, color, myTurtle)
    count=degree
    while count > 0:
        #degree 1 3 circles

        radius1 = radius / (1+math.sqrt(2))
        new_x = point[0] + radius1
        new_y = point[1] + radius-(2*radius1)
        new_point = [new_x, new_y]
        drawCircle(new_point, radius1, color, myTurtle,)
        new_x = point[0] - radius1
        new_y = point[1] + radius
        new_point = [new_x, new_y]
        drawCircle(new_point, radius1, color, myTurtle)
        new_x = point[0] + radius1
        new_y = point[1] + radius
        new_point = [new_x, new_y]
        drawCircle(new_point, radius1, color, myTurtle)
        count= count-1
        break


    while count>0:
        #degree 2 top left
        radius1 = radius / (1 + math.sqrt(2))
        radius2 = radius1 / (1 + math.sqrt(2))
        new_x = point[0] + radius2 - radius1
        new_y = point[1] + radius1 +radius
        new_point = [new_x, new_y]
        drawCircle(new_point, radius2, color, myTurtle),
        new_x = point[0] + radius2 - radius1
        new_y = point[1] + radius1 - (2 * radius2) +radius
        new_point = [new_x, new_y]
        drawCircle(new_point, radius2, color, myTurtle)
        new_x = point[0] - radius2 - radius1
        new_y = point[1] + radius1 - (2 * radius2)+radius
        new_point = [new_x, new_y]
        drawCircle(new_point, radius2, color, myTurtle),
        #degree 2 top right
        new_x = point[0] + radius2 + radius1
        new_y = point[1] + radius1 + radius
        new_point = [new_x, new_y]
        drawCircle(new_point, radius2, color, myTurtle),
        new_x = point[0] + radius2 + radius1
        new_y = point[1] + radius1 - (2 * radius2) + radius
        new_point = [new_x, new_y]
        drawCircle(new_point, radius2, color, myTurtle)
        new_x = point[0] - radius2 + radius1
        new_y = point[1] + radius1 - (2 * radius2) + radius
        new_point = [new_x, new_y]
        drawCircle(new_point, radius2, color, myTurtle),
        # degree 2 bottomright
        new_x = point[0] + radius2 + radius1
        new_y = point[1] + radius1 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius2, color, myTurtle),
        new_x = point[0] + radius2 + radius1
        new_y = point[1] + radius1 - (2 * radius2) + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius2, color, myTurtle)
        new_x = point[0] - radius2 + radius1
        new_y = point[1] + radius1 - (2 * radius2) + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius2, color, myTurtle),
        count = count - 1
        break


    while count>0:
        radius1 = radius / (1 + math.sqrt(2))
        radius2 = radius1 / (1 + math.sqrt(2))
        radius3 = radius2 / (1 + math.sqrt(2))
        #degree 3 bottom right, for bottom right of top left
        new_x = point[0] + radius3 - radius1 + radius2
        new_y = point[1] + radius2 - (2 * radius3)+radius +radius3
        new_point = [new_x, new_y]
        drawCircle(new_point, radius3, color, myTurtle)
        # degree 3 bottom left, for bottom right of top left
        new_x = point[0] - radius3 - radius1 +radius2
        new_y = point[1] + radius2 - (2 * radius3) +radius +radius3
        new_point = [new_x, new_y]
        drawCircle(new_point, radius3, color, myTurtle),
        # degree 3 top left, for bottom right of top left
        new_x = point[0] - radius3 - radius1+radius2
        new_y = point[1] + radius2 +radius+radius3
        new_point = [new_x, new_y]
        drawCircle(new_point, radius3, color, myTurtle)

        # degree 3 bottom right, for bottom left of top left
        new_x = point[0] + radius3 - radius1 - radius2
        new_y = point[1] + radius2 - (2 * radius3) + radius + radius3
        new_point = [new_x, new_y]
        drawCircle(new_point, radius3, color, myTurtle)
        # degree 3 bottom left, for bottom left of top left
        new_x = point[0] - radius3 - radius1 - radius2
        new_y = point[1] + radius2 - (2 * radius3) + radius + radius3
        new_point = [new_x, new_y]
        drawCircle(new_point, radius3, color, myTurtle),
        # degree 3 top left, for bottom left of top left
        new_x = point[0] - radius3 - radius1 - radius2
        new_y = point[1] + radius2 + radius + radius3
        new_point = [new_x, new_y]
        drawCircle(new_point, radius3, color, myTurtle)

        # degree 3 bottom right, for bottom right of top left
        new_x = point[0] + radius3 - radius1 + radius2
        new_y = point[1] + radius2 - (2 * radius3) + radius + radius1
        new_point = [new_x, new_y]
        drawCircle(new_point, radius3, color, myTurtle)
        # degree 3 bottom left, for bottom right of top left
        new_x = point[0] - radius3 - radius1 + radius2
        new_y = point[1] + radius2 - (2 * radius3) + radius + radius1
        new_point = [new_x, new_y]
        drawCircle(new_point, radius3, color, myTurtle),
        # degree 3 top left, for bottom right of top left
        new_x = point[0] - radius3 - radius1 + radius2
        new_y = point[1] + radius2 + radius + radius1
        new_point = [new_x, new_y]
        drawCircle(new_point, radius3, color, myTurtle)

        # degree 3 top right
        new_x = point[0] + radius3 - radius1 + radius
        new_y = point[1] + radius2 - (2 * radius3) + radius + radius3
        new_point = [new_x, new_y]
        drawCircle(new_point, radius3, color, myTurtle)
        new_x = point[0] - radius3 - radius1 + radius
        new_y = point[1] + radius2 - (2 * radius3) + radius + radius3
        new_point = [new_x, new_y]
        drawCircle(new_point, radius3, color, myTurtle),
        new_x = point[0] - radius3 - radius1 + radius2 + radius -radius2
        new_y = point[1] + radius2 + radius + radius3
        new_point = [new_x, new_y]
        drawCircle(new_point, radius3, color, myTurtle)

        new_x = point[0] + radius3 - radius1 - radius2 +radius-radius2
        new_y = point[1] + radius2 - (2 * radius3) + radius + radius3
        new_point = [new_x, new_y]
        drawCircle(new_point, radius3, color, myTurtle)
        new_x = point[0] - radius3 - radius1 - radius2+radius-radius2
        new_y = point[1] + radius2 - (2 * radius3) + radius + radius3
        new_point = [new_x, new_y]
        drawCircle(new_point, radius3, color, myTurtle),
        new_x = point[0] - radius3 - radius1 - radius2+radius-radius2
        new_y = point[1] + radius2 + radius + radius3
        new_point = [new_x, new_y]
        drawCircle(new_point, radius3, color, myTurtle)

        new_x = point[0] + radius3 - radius1 + radius2+radius-radius2
        new_y = point[1] + radius2 - (2 * radius3) + radius + radius1
        new_point = [new_x, new_y]
        drawCircle(new_point, radius3, color, myTurtle)
        new_x = point[0] - radius3 - radius1 + radius2+radius-radius2
        new_y = point[1] + radius2 - (2 * radius3) + radius + radius1
        new_point = [new_x, new_y]
        drawCircle(new_point, radius3, color, myTurtle),
        new_x = point[0] - radius3 - radius1 + radius2+radius-radius2
        new_y = point[1] + radius2 + radius + radius1
        new_point = [new_x, new_y]
        drawCircle(new_point, radius3, color, myTurtle)

        # degree 3 bottom right
        new_x = point[0] + radius3 - radius1 + radius
        new_y = point[1] + radius2 - (2 * radius3) + radius + radius3 -radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius3, color, myTurtle)
        new_x = point[0] - radius3 - radius1 + radius
        new_y = point[1] + radius2 - (2 * radius3) + radius + radius3-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius3, color, myTurtle),
        new_x = point[0] - radius3 - radius1 + radius2 + radius - radius2
        new_y = point[1] + radius2 + radius + radius3-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius3, color, myTurtle)

        new_x = point[0] + radius3 - radius1 - radius2 + radius - radius2
        new_y = point[1] + radius2 - (2 * radius3) + radius + radius3-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius3, color, myTurtle)
        new_x = point[0] - radius3 - radius1 - radius2 + radius - radius2
        new_y = point[1] + radius2 - (2 * radius3) + radius + radius3-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius3, color, myTurtle),
        new_x = point[0] - radius3 - radius1 - radius2 + radius - radius2
        new_y = point[1] + radius2 + radius + radius3-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius3, color, myTurtle)

        new_x = point[0] + radius3 - radius1 + radius2 + radius - radius2
        new_y = point[1] + radius2 - (2 * radius3) + radius + radius1 -radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius3, color, myTurtle)
        new_x = point[0] - radius3 - radius1 + radius2 + radius - radius2
        new_y = point[1] + radius2 - (2 * radius3) + radius + radius1-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius3, color, myTurtle),
        new_x = point[0] - radius3 - radius1 + radius2 + radius - radius2
        new_y = point[1] + radius2 + radius + radius1-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius3, color, myTurtle)
        count = count - 1
        break

    while count>0:
        #degree 4
        radius1 = radius / (1 + math.sqrt(2))
        radius2 = radius1 / (1 + math.sqrt(2))
        radius3 = radius2 / (1 + math.sqrt(2))
        radius4 = radius3 / (1 + math.sqrt(2))
        new_x = point[0] - radius4 -radius+radius1-radius3
        new_y = point[1] + radius3 - (2 * radius4)+radius+radius3+radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4-radius+radius1-radius3
        new_y = point[1] + radius3+radius+radius3+radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] + radius4-radius+radius1-radius3
        new_y = point[1] + radius3+radius+radius3+radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3+radius2-radius4
        new_y = point[1] + radius3 - (2 * radius4) + radius + radius3 + radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3+radius2-radius4
        new_y = point[1] + radius3 + radius + radius3 + radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] + radius4 - radius + radius1 - radius3+radius2-radius4
        new_y = point[1] + radius3 + radius + radius3 + radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3
        new_y = point[1] + radius3 - (2 * radius4) + radius + radius3 + radius4 +radius2-radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3
        new_y = point[1] + radius3 + radius + radius3 + radius4+radius2-radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] + radius4 - radius + radius1 - radius3
        new_y = point[1] + radius3 + radius + radius3 + radius4+radius2-radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)

        radius4 = radius3 / (1 + math.sqrt(2))
        new_x = point[0] - radius4 - radius + radius1 - radius3+radius1-radius3
        new_y = point[1] + radius3 - (2 * radius4) + radius + radius3 + radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3+radius1-radius3
        new_y = point[1] + radius3 + radius + radius3 + radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] + radius4 - radius + radius1 - radius3+radius1-radius3
        new_y = point[1] + radius3 + radius + radius3 + radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3 + radius2 - radius4+radius1-radius3
        new_y = point[1] + radius3 - (2 * radius4) + radius + radius3 + radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3 + radius2 - radius4+radius1-radius3
        new_y = point[1] + radius3 + radius + radius3 + radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] + radius4 - radius + radius1 - radius3 + radius2 - radius4+radius1-radius3
        new_y = point[1] + radius3 + radius + radius3 + radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3+radius1-radius3
        new_y = point[1] + radius3 - (2 * radius4) + radius + radius3 + radius4 + radius2 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3+radius1-radius3
        new_y = point[1] + radius3 + radius + radius3 + radius4 + radius2 -radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] + radius4 - radius + radius1 - radius3+radius1-radius3
        new_y = point[1] + radius3 + radius + radius3 + radius4 + radius2 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)


        new_x = point[0] - radius4 - radius + radius1 - radius3 + radius1 - radius3
        new_y = point[1] + radius3 - (2 * radius4) + radius + radius3 + radius4+ radius1 - radius3
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3 + radius1 - radius3
        new_y = point[1] + radius3 + radius + radius3 + radius4+ radius1 - radius3
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] + radius4 - radius + radius1 - radius3 + radius1 - radius3
        new_y = point[1] + radius3 + radius + radius3 + radius4+ radius1 - radius3
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3 + radius2 - radius4 + radius1 - radius3
        new_y = point[1] + radius3 - (2 * radius4) + radius + radius3 + radius4+ radius1 - radius3
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3 + radius2 - radius4 + radius1 - radius3
        new_y = point[1] + radius3 + radius + radius3 + radius4+ radius1 - radius3
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] + radius4 - radius + radius1 - radius3 + radius2 - radius4 + radius1 - radius3
        new_y = point[1] + radius3 + radius + radius3 + radius4+ radius1 - radius3
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3 + radius1 - radius3
        new_y = point[1] + radius3 - (2 * radius4) + radius + radius3 + radius4 + radius2 - radius4+ radius1 - radius3
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3 + radius1 - radius3
        new_y = point[1] + radius3 + radius + radius3 + radius4 + radius2 - radius4+ radius1 - radius3
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] + radius4 - radius + radius1 - radius3 + radius1 - radius3
        new_y = point[1] + radius3 + radius + radius3 + radius4 + radius2 - radius4+ radius1 - radius3
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)


#degree 4 right
        radius4 = radius3 / (1 + math.sqrt(2))
        new_x = point[0] - radius4 - radius + radius1 - radius3+radius-radius2
        new_y = point[1] + radius3 - (2 * radius4) + radius + radius3 + radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3+radius-radius2
        new_y = point[1] + radius3 + radius + radius3 + radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] + radius4 - radius + radius1 - radius3+radius-radius2
        new_y = point[1] + radius3 + radius + radius3 + radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3 + radius2 - radius4+radius-radius2
        new_y = point[1] + radius3 - (2 * radius4) + radius + radius3 + radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3 + radius2 - radius4+radius-radius2
        new_y = point[1] + radius3 + radius + radius3 + radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] + radius4 - radius + radius1 - radius3 + radius2 - radius4+radius-radius2
        new_y = point[1] + radius3 + radius + radius3 + radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3+radius-radius2
        new_y = point[1] + radius3 - (2 * radius4) + radius + radius3 + radius4 + radius2 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3+radius-radius2
        new_y = point[1] + radius3 + radius + radius3 + radius4 + radius2 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] + radius4 - radius + radius1 - radius3+radius-radius2
        new_y = point[1] + radius3 + radius + radius3 + radius4 + radius2 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)


        new_x = point[0] - radius4 - radius + radius1 - radius3 + radius1 - radius3+radius-radius2
        new_y = point[1] + radius3 - (2 * radius4) + radius + radius3 + radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3 + radius1 - radius3+radius-radius2
        new_y = point[1] + radius3 + radius + radius3 + radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] + radius4 - radius + radius1 - radius3 + radius1 - radius3+radius-radius2
        new_y = point[1] + radius3 + radius + radius3 + radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3 + radius2 - radius4 + radius1 - radius3+radius-radius2
        new_y = point[1] + radius3 - (2 * radius4) + radius + radius3 + radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3 + radius2 - radius4 + radius1 - radius3+radius-radius2
        new_y = point[1] + radius3 + radius + radius3 + radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] + radius4 - radius + radius1 - radius3 + radius2 - radius4 + radius1 - radius3+radius-radius2
        new_y = point[1] + radius3 + radius + radius3 + radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3 + radius1 - radius3+radius-radius2
        new_y = point[1] + radius3 - (2 * radius4) + radius + radius3 + radius4 + radius2 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3 + radius1 - radius3+radius-radius2
        new_y = point[1] + radius3 + radius + radius3 + radius4 + radius2 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] + radius4 - radius + radius1 - radius3 + radius1 - radius3+radius-radius2
        new_y = point[1] + radius3 + radius + radius3 + radius4 + radius2 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)

        new_x = point[0] - radius4 - radius + radius1 - radius3 + radius1 - radius3+radius-radius2
        new_y = point[1] + radius3 - (2 * radius4) + radius + radius3 + radius4 + radius1 - radius3
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3 + radius1 - radius3+radius-radius2
        new_y = point[1] + radius3 + radius + radius3 + radius4 + radius1 - radius3
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] + radius4 - radius + radius1 - radius3 + radius1 - radius3+radius-radius2
        new_y = point[1] + radius3 + radius + radius3 + radius4 + radius1 - radius3
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3 + radius2 - radius4 + radius1 - radius3+radius-radius2
        new_y = point[1] + radius3 - (2 * radius4) + radius + radius3 + radius4 + radius1 - radius3
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3 + radius2 - radius4 + radius1 - radius3+radius-radius2
        new_y = point[1] + radius3 + radius + radius3 + radius4 + radius1 - radius3
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] + radius4 - radius + radius1 - radius3 + radius2 - radius4 + radius1 - radius3+radius-radius2
        new_y = point[1] + radius3 + radius + radius3 + radius4 + radius1 - radius3
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3 + radius1 - radius3+radius-radius2
        new_y = point[1] + radius3 - (2 * radius4) + radius + radius3 + radius4 + radius2 - radius4 + radius1 - radius3
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3 + radius1 - radius3+radius-radius2
        new_y = point[1] + radius3 + radius + radius3 + radius4 + radius2 - radius4 + radius1 - radius3
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] + radius4 - radius + radius1 - radius3 + radius1 - radius3+radius-radius2
        new_y = point[1] + radius3 + radius + radius3 + radius4 + radius2 - radius4 + radius1 - radius3
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)

        #degree 4 3
        radius4 = radius3 / (1 + math.sqrt(2))
        new_x = point[0] - radius4 - radius + radius1 - radius3 + radius - radius2
        new_y = point[1] + radius3 - (2 * radius4) + radius + radius3 + radius4- radius + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3 + radius - radius2
        new_y = point[1] + radius3 + radius + radius3 + radius4- radius + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] + radius4 - radius + radius1 - radius3 + radius - radius2
        new_y = point[1] + radius3 + radius + radius3 + radius4- radius + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3 + radius2 - radius4 + radius - radius2
        new_y = point[1] + radius3 - (2 * radius4) + radius + radius3 + radius4- radius + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3 + radius2 - radius4 + radius - radius2
        new_y = point[1] + radius3 + radius + radius3 + radius4- radius + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] + radius4 - radius + radius1 - radius3 + radius2 - radius4 + radius - radius2
        new_y = point[1] + radius3 + radius + radius3 + radius4- radius + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3 + radius - radius2
        new_y = point[1] + radius3 - (2 * radius4) + radius + radius3 + radius4 + radius2 - radius4- radius + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3 + radius - radius2
        new_y = point[1] + radius3 + radius + radius3 + radius4 + radius2 - radius4- radius + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] + radius4 - radius + radius1 - radius3 + radius - radius2
        new_y = point[1] + radius3 + radius + radius3 + radius4 + radius2 - radius4- radius + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)

        new_x = point[0] - radius4 - radius + radius1 - radius3 + radius1 - radius3 + radius - radius2
        new_y = point[1] + radius3 - (2 * radius4) + radius + radius3 + radius4- radius + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3 + radius1 - radius3 + radius - radius2
        new_y = point[1] + radius3 + radius + radius3 + radius4- radius + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] + radius4 - radius + radius1 - radius3 + radius1 - radius3 + radius - radius2
        new_y = point[1] + radius3 + radius + radius3 + radius4- radius + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[
                    0] - radius4 - radius + radius1 - radius3 + radius2 - radius4 + radius1 - radius3 + radius - radius2
        new_y = point[1] + radius3 - (2 * radius4) + radius + radius3 + radius4- radius + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[
                    0] - radius4 - radius + radius1 - radius3 + radius2 - radius4 + radius1 - radius3 + radius - radius2
        new_y = point[1] + radius3 + radius + radius3 + radius4- radius + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[
                    0] + radius4 - radius + radius1 - radius3 + radius2 - radius4 + radius1 - radius3 + radius - radius2
        new_y = point[1] + radius3 + radius + radius3 + radius4- radius + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3 + radius1 - radius3 + radius - radius2
        new_y = point[1] + radius3 - (2 * radius4) + radius + radius3 + radius4 + radius2 - radius4- radius + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3 + radius1 - radius3 + radius - radius2
        new_y = point[1] + radius3 + radius + radius3 + radius4 + radius2 - radius4- radius + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] + radius4 - radius + radius1 - radius3 + radius1 - radius3 + radius - radius2
        new_y = point[1] + radius3 + radius + radius3 + radius4 + radius2 - radius4- radius + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)

        new_x = point[0] - radius4 - radius + radius1 - radius3 + radius1 - radius3 + radius - radius2
        new_y = point[1] + radius3 - (2 * radius4) + radius + radius3 + radius4 + radius1 - radius3- radius + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3 + radius1 - radius3 + radius - radius2
        new_y = point[1] + radius3 + radius + radius3 + radius4 + radius1 - radius3- radius + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] + radius4 - radius + radius1 - radius3 + radius1 - radius3 + radius - radius2
        new_y = point[1] + radius3 + radius + radius3 + radius4 + radius1 - radius3- radius + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[
                    0] - radius4 - radius + radius1 - radius3 + radius2 - radius4 + radius1 - radius3 + radius - radius2
        new_y = point[1] + radius3 - (2 * radius4) + radius + radius3 + radius4 + radius1 - radius3- radius + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[
                    0] - radius4 - radius + radius1 - radius3 + radius2 - radius4 + radius1 - radius3 + radius - radius2
        new_y = point[1] + radius3 + radius + radius3 + radius4 + radius1 - radius3- radius + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[
                    0] + radius4 - radius + radius1 - radius3 + radius2 - radius4 + radius1 - radius3 + radius - radius2
        new_y = point[1] + radius3 + radius + radius3 + radius4 + radius1 - radius3- radius + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3 + radius1 - radius3 + radius - radius2
        new_y = point[1] + radius3 - (2 * radius4) + radius + radius3 + radius4 + radius2 - radius4 + radius1 - radius3- radius + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] - radius4 - radius + radius1 - radius3 + radius1 - radius3 + radius - radius2
        new_y = point[1] + radius3 + radius + radius3 + radius4 + radius2 - radius4 + radius1 - radius3- radius + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        new_x = point[0] + radius4 - radius + radius1 - radius3 + radius1 - radius3 + radius - radius2
        new_y = point[1] + radius3 + radius + radius3 + radius4 + radius2 - radius4 + radius1 - radius3- radius + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius4, color, myTurtle)
        count = count - 1
        break

    while count>0:
        #degree 5
        radius1 = radius / (1 + math.sqrt(2))
        radius2 = radius1 / (1 + math.sqrt(2))
        radius3 = radius2 / (1 + math.sqrt(2))
        radius4 = radius3 / (1 + math.sqrt(2))
        radius5 = radius4 / (1 + math.sqrt(2))

        new_x = point[0] - radius5 - radius +radius2 +radius3 +radius4+radius4+radius5
        new_y = point[1] + radius4 + radius +radius4 +radius2 -radius3 +radius4 +radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius +radius2 +radius3 +radius4+radius4+radius5
        new_y = point[1] + radius4+ radius +radius4 +radius2 -radius3 +radius4+radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius +radius2 +radius3 +radius4+radius4+radius5
        new_y = point[1] + radius4-(2*radius5)+ radius +radius4 +radius2 -radius3 +radius4+radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5+radius4+radius4
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5+radius4+radius4
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5+radius4+radius4
        new_y = point[1] + radius4 - (2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius +radius2 +radius3 +radius4+radius4+radius5
        new_y = point[1] + radius4 + radius +radius4 +radius2 -radius3 +radius4 +radius5-radius4-radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius +radius2 +radius3 +radius4+radius4+radius5
        new_y = point[1] + radius4+ radius +radius4 +radius2 -radius3 +radius4+radius5-radius4-radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius +radius2 +radius3 +radius4+radius4+radius5
        new_y = point[1] + radius4-(2*radius5)+ radius +radius4 +radius2 -radius3 +radius4+radius5-radius4-radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5+radius2-radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5+radius2-radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5
        new_y = point[1] + radius4 - (2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5+radius2-radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5+radius2-radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5+radius2-radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4
        new_y = point[1] + radius4 - (2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5+radius2-radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4+radius2-radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4+radius2-radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5
        new_y = point[1] + radius4 - (2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4+radius2-radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5+radius2-radius4
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5+radius2-radius4
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5+radius2-radius4
        new_y = point[1] + radius4 - (2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4+radius2-radius4
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4+radius2-radius4
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4+radius2-radius4
        new_y = point[1] + radius4 - (2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius +radius2 +radius3 +radius4+radius4+radius5+radius2-radius4
        new_y = point[1] + radius4 + radius +radius4 +radius2 -radius3 +radius4 +radius5-radius4-radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius +radius2 +radius3 +radius4+radius4+radius5+radius2-radius4
        new_y = point[1] + radius4+ radius +radius4 +radius2 -radius3 +radius4+radius5-radius4-radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius +radius2 +radius3 +radius4+radius4+radius5+radius2-radius4
        new_y = point[1] + radius4-(2*radius5)+ radius +radius4 +radius2 -radius3 +radius4+radius5-radius4-radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5+radius2+radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5+radius2+radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5+radius2+radius2
        new_y = point[1] + radius4 - (2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4+radius2+radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4+radius2+radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4+radius2+radius2
        new_y = point[1] + radius4 - (2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5+radius2+radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5+radius2+radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5+radius2+radius2
        new_y = point[1] + radius4 - (2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5+radius2+radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5+radius2+radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5+radius2+radius2
        new_y = point[1] + radius4 - (2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4+radius2+radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4+radius2+radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4+radius2+radius2
        new_y = point[1] + radius4 - (
                    2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5+radius2+radius2
        new_y = point[
                    1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4 + radius2 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5+radius2+radius2
        new_y = point[
                    1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4 + radius2 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5+radius2+radius2
        new_y = point[1] + radius4 - (
                    2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4 + radius2 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4+radius2+radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4+radius2+radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4+radius2+radius2
        new_y = point[1] + radius4 - (2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 - radius4+radius2+radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 - radius4+radius2+radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 - radius4+radius2+radius2
        new_y = point[1] + radius4 - (2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4+radius2+radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4+radius2+radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4+radius2+radius2
        new_y = point[1] + radius4 - (2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5+radius2+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5+radius2+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2
        new_y = point[1] + radius4 - (2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5+radius2+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 + radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5+radius2+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 + radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5+radius2+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 + radius2
        new_y = point[1] + radius4 - (2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5+radius2+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4+radius2+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4+radius2+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2
        new_y = point[1] + radius4 - (2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4+radius2+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4+ radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4+ radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2
        new_y = point[1] + radius4 - (
                    2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4+ radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 + radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4+ radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 + radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4+ radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 + radius2
        new_y = point[1] + radius4 - (
                2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4+ radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2
        new_y = point[
                    1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4 + radius2 - radius4+ radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2
        new_y = point[
                    1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4 + radius2 - radius4+ radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2
        new_y = point[1] + radius4 - (
                2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4 + radius2 - radius4+ radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5+ radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5+ radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2
        new_y = point[1] + radius4 - (2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5+ radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 - radius4 + radius2 + radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5+ radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 - radius4 + radius2 + radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5+ radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 - radius4 + radius2 + radius2
        new_y = point[1] + radius4 - (2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5+ radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4+ radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4+ radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2
        new_y = point[1] + radius4 - (
                    2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4+ radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5+radius-radius2
        new_y = point[1] + radius4 - (2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4+radius-radius2
        new_y = point[1] + radius4 - (2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5+radius-radius2
        new_y = point[1] + radius4 - (
                    2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5+radius-radius2
        new_y = point[1] + radius4 - (
                    2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4+radius-radius2
        new_y = point[1] + radius4 - (
                    2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5+radius-radius2
        new_y = point[
                    1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4 + radius2 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5+radius-radius2
        new_y = point[
                    1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4 + radius2 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5+radius-radius2
        new_y = point[1] + radius4 - (
                    2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4 + radius2 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4+radius-radius2
        new_y = point[1] + radius4 - (2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 - radius4+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 - radius4+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 - radius4+radius-radius2
        new_y = point[1] + radius4 - (2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4+radius-radius2
        new_y = point[1] + radius4 - (
                    2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 - (2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 - (2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 - (
                    2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 - (
                    2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 - (
                2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2+radius-radius2
        new_y = point[
                    1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4 + radius2 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2+radius-radius2
        new_y = point[
                    1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4 + radius2 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 - (
                2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4 + radius2 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 - (2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 - radius4 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 - radius4 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 - radius4 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 - (2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 - (
                    2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 - (
                    2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 - (
                    2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2+radius-radius2
        new_y = point[
                    1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4 + radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2+radius-radius2
        new_y = point[
                    1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4 + radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 - (
                    2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4 + radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2+radius-radius2
        new_y = point[
                    1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2+radius-radius2
        new_y = point[
                    1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 - (
                2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 + radius2+radius-radius2
        new_y = point[
                    1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 + radius2+radius-radius2
        new_y = point[
                    1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 - (
                2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2+radius-radius2
        new_y = point[
                    1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4 + radius2 - radius4 + radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2+radius-radius2
        new_y = point[
                    1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4 + radius2 - radius4 + radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 - (
                2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4 + radius2 - radius4 + radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 - (
                    2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 - radius4 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 - radius4 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 - radius4 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 - (
                    2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2+radius-radius2
        new_y = point[
                    1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4 + radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2+radius-radius2
        new_y = point[
                    1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4 + radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2+radius-radius2
        new_y = point[1] + radius4 - (
                2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4 + radius2 + radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)

        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius - radius2
        new_y = point[1] + radius4 - (2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius - radius2
        new_y = point[1] + radius4 - (2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius - radius2
        new_y = point[1] + radius4 - (
                2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius - radius2
        new_y = point[1] + radius4 - (
                2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius - radius2
        new_y = point[1] + radius4 - (
                2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius - radius2
        new_y = point[
                    1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4 + radius2 - radius4-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius - radius2
        new_y = point[
                    1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4 + radius2 - radius4-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius - radius2
        new_y = point[1] + radius4 - (
                2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4 + radius2 - radius4-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4 + radius - radius2
        new_y = point[1] + radius4 - (2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 - radius4 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 - radius4 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 - radius4 + radius - radius2
        new_y = point[1] + radius4 - (2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4 + radius - radius2
        new_y = point[1] + radius4 - (
                2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 - (2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 - (2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 - (
                2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 - (
                2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 - (
                2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2 + radius - radius2
        new_y = point[
                    1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4 + radius2 - radius4-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2 + radius - radius2
        new_y = point[
                    1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4 + radius2 - radius4-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 - (
                2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4 + radius2 - radius4-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 - (2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 - radius4 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 - radius4 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 - radius4 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 - (2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 - (
                2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 + radius2-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 + radius2-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 - (
                2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 + radius2-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 + radius2-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 + radius2-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 - (
                2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 + radius2-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2 + radius - radius2
        new_y = point[
                    1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4 + radius2 + radius2-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2 + radius - radius2
        new_y = point[
                    1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4 + radius2 + radius2-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 - (
                2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4 + radius2 + radius2-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2 + radius - radius2
        new_y = point[
                    1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2 + radius - radius2
        new_y = point[
                    1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 - (
                2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 + radius2 + radius - radius2
        new_y = point[
                    1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 + radius2 + radius - radius2
        new_y = point[
                    1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 - (
                2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2 + radius - radius2
        new_y = point[
                    1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4 + radius2 - radius4 + radius2 + radius2-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2 + radius - radius2
        new_y = point[
                    1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4 + radius2 - radius4 + radius2 + radius2-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 - (
                2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4 + radius2 - radius4 + radius2 + radius2-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 + radius2-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 + radius2-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 - (
                2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 + radius2-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 - radius4 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 + radius2-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 - radius4 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 + radius2-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius4 + radius4 + radius2 - radius4 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 - (
                2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 + radius2 + radius2-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] - radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2 + radius - radius2
        new_y = point[
                    1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4 + radius2 + radius2-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2 + radius - radius2
        new_y = point[
                    1] + radius4 + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4 + radius2 + radius2-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)
        new_x = point[
                    0] + radius5 - radius + radius2 + radius3 + radius4 + radius4 + radius5 + radius2 - radius4 + radius2 + radius2 + radius - radius2
        new_y = point[1] + radius4 - (
                2 * radius5) + radius + radius4 + radius2 - radius3 + radius4 + radius5 - radius4 - radius4 + radius2 + radius2-radius+radius2
        new_point = [new_x, new_y]
        drawCircle(new_point, radius5, color, myTurtle)

        count = count-1
        break

def main():
    myTurtle = turtle.Turtle()
    myTurtle.speed(0)
    myWin = turtle.Screen()
    point = [0,0]
    radius = 150
    degree = 4
    sierpinskiCircle(point, radius, degree, "blue", myTurtle)
    myTurtle.hideturtle()  # hide the turtle cursor after drawing is completed
    myWin.exitonclick()  # Exit program when user click on window

main()
