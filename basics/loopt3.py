from turtle import *
speed(0)
pencolor("red")
bgcolor("black")
val = 1
while True:
    forward(3 * val)
    left(360/3)
    #dot(10)
    circle(2,100)
    val += 1