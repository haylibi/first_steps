from turtle import *

def passeio(n,a):
    import random
    import turtle
    for i in range(n):
        w=0.5*window_width()
        h=0.5*window_height()
        x=xcor()
        y=ycor()
        if x<w and x+w>=0 and y<w and y+w>=0:
            turtle.forward(10)
            turtle.left(random.randint(-a,a))
        if x>w or x<-w:
            turtle.penup()
            turtle.setposition(-x,y)
            angulo=turtle.towards(0,0)
            turtle.setheading(angulo)
            turtle.pendown()
            turtle.forward(10)
        if y>h or y<-h:
            turtle.penup()
            turtle.setposition(x,-y)
            turtle.setheading(turtle.towards(0,0))
            turtle.pendown()
            turtle.forward(10)


def snake(n):
    import random
    import turtle
    angulos = [90,-90,0]
    turtle.speed=100
    for i in range(n):
        w=0.5*window_width()
        h=0.5*window_height()
        x=xcor()
        y=ycor()
        if x<w and x+w>=0 and y<w and y+w>=0:
            turtle.forward(20)
            a=random.sample(angulos,1)
            turtle.left(a[0])
        if x>w or x<-w:
            turtle.penup()
            turtle.setposition(-x,y)
            if x>0:
                turtle.setheading(0)
            if x<0:
                turtle.setheading(180)
            turtle.pendown()
            turtle.forward(10)
        if y>h or y<-h:
            turtle.penup()
            turtle.setposition(x,-y)
            if y>0:
                turtle.setheading(90)
            if y<0:
                turtle.setheading(-90)
            turtle.pendown()
            turtle.forward(10)
