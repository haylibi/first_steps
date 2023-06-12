import turtle
from random import*
def turtle_random(figuras):
    turtle.Terminator
    cores = ['green','yellow','purple','black','blue','red','pink','orange']
    def quadrado(n):
        for i in range(4):
            turtle.color(sample(cores, 1))
            turtle.forward(n)
            turtle.left(90)
    def poligno(n,lado):
        for i in range(n):
            turtle.forward(lado)
            turtle.left(360/n)
    def lozango(n):
        for i in [60,60,120,60]:
            turtle.color('red')
            turtle.left(i)
            turtle.forward(n)
    def estrela(n):
        for i in range(5):
            turtle.forward(n)
            turtle.right(144)
    def fig_rand(n):
        while n>10:
            n=n-5
        for i in range(randint(3,4)):
            turtle.penup()
            turtle.left(randint(-180,180))
            turtle.forward(randint(3*n,5*n))
            turtle.pendown()
    for i in range(figuras):
        a=randint(1,6)
        if a==1:
            quadrado(randint(100,200))
            fig_rand(randint(1,50))
        if a==2:
            lozango(randint(100,200))
            fig_rand(randint(1,50))
        if a==3:
            estrela(randint(100,200))
            fig_rand(randint(1,50))
        if a==4:
            turtle.circle(randint(100,200))
            fig_rand(randint(1,50))
        if a==5:
            poligno(randint(5,9),randint(50,100))
            fig_rand(randint(1,50))
