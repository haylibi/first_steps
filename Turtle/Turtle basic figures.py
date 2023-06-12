import turtle
import math
from random import*
cores = ['green','red','purple','yellow','black','blue','orange','green','gray','brown','pink']
def triangulo(n):
    '''Triangulo Equilatero perimetro 3n'''
    for i in range(3):
        turtle.forward(n)
        turtle.left(120)

def quadrado(n):
    '''Quadrado de lado n'''
    for i in range(4):
        turtle.forward(n)
        turtle.left(90)
def casa(n):
    '''casa lado n'''
    quadrado(n)
    for i in range(3):
        turtle.forward(n)
        turtle.left(90)
    turtle.left(90)
    triangulo(n)
def triforce(n):
    '''Simbolo Tri-Force lado n'''
    for i in range(2):
        triangulo(n)
        turtle.forward(n)
    turtle.left(120)
    turtle.forward(n)
    turtle.left(60)
    turtle.forward(n)
    turtle.right(180)
    triangulo(n)
    turtle.right(60)
    turtle.forward(n)
def poligno(n, lado):
    '''Poligno com n vertices de perimetro n.lado'''
    for i in range(n):
        turtle.forward(lado)
        turtle.left(360/n)
def estrela(n):
    '''estrela de lado n'''
    for i in range(5):
        turtle.forward(n)
        turtle.right(144)
def estrela_i(n):
    '''estrela de lado n'''
    for i in range(5):
        turtle.forward(n)
        turtle.left(144)
def friso(n, lado):
    for i in range(n):
        turtle.forward(lado)
        turtle.left(90)
        turtle.forward(lado)
        for i in range(2):
            turtle.right(90)
            turtle.forward(lado)
        turtle.left(90)
def estrela_e(n):
	for i in range(n):
		for o in range(5):
			estrela(100+i*10)
			turtle.left(144)
def estrela_s(n):
    for i in range(5):
        turtle.forward(n)
        turtle.left(72)
        turtle.forward(n)
        turtle.right(144)
def estrela_sn(n):
    for i in range(n):
        turtle.color(sample(cores,1))
        for o in range(5):
            estrela_s(10+i*5)
            turtle.left(144)
#figura estranha
for i in range(1,100):
	turtle.forward(100-80/i)
	turtle.right(90-80/i)
	lozango(i)

