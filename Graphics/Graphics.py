import turtle
import colorsys

turtle.tracer(2)
turtle.bgcolor('black')
turtle.pensize(2)
n=100
h=0
for i in range (500):
    for i in range (4):
        c = colorsys.hsv_to_rgb(h,1,1)
        h += 1/n
        turtle.color(c)
        turtle.circle(49+i*5,90)
        turtle.forward(100)
        turtle.left(90)
    turtle.right(10)
turtle.done()