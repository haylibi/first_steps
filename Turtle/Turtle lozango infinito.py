from random import*
import turtle
cores = ['green','purple','black','blue','red','pink','orange']
def lozango2(n):
    def lozango(n):
            turtle.left(60)
            turtle.penup()
            turtle.forward(n)
            turtle.pendown()
            turtle.left(60)
            turtle.forward(n)
            turtle.left(120)
            turtle.forward(n)
            turtle.penup()
            turtle.left(60)
            turtle.forward(n)
            turtle.pendown()
    def lozango1(n):
        for i in range(6):
            lozango(n)
    for i in range(n):
        turtle.speed=10+i
        turtle.color(sample(cores, 1))
        lozango1(5+5*i)

def lozango(n):
    for i in [60,60,120,60]:
        turtle.left(i)
        turtle.forward(n)
