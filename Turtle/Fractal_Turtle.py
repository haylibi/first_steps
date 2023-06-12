#Quase fractal que tristao falou
import turtle
def fractal(n,t):
	turtle.speed(30)
	turtle.setheading(t)
	if n==1:
		turtle.forward(4)
	else:
		fractal(n-1,t)
		fractal(n-1,(t+90)%360)
