
import turtle

t = turtle.Turtle()

# setting turtle to left  side of canvas
t.penup()
t.setx(-300)
t.pendown()


def drawline(length):

    t.forward(length)


def shape(length, rec, counter=0):

    if counter < rec:
        drawline(length)
        t.left(60)
        drawline(length)
        t.right(120)
        drawline(length)
        t.left(60)
        drawline(length)
    else:

        for i in range(rec):
            length = length/2
            counter = i
            shape(length,rec,counter)


def fractal(size, angle):


    shape(size,angle)
    t.left(angle)
    shape(size,angle)
    t.right(angle * 2)
    shape(size,angle)
    t.left(angle)
    shape(size,angle)

fractal(200,60)

turtle.done()







