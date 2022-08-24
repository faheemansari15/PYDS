from turtle import *

colors = ['red', 'blue', 'yellow', 'black']
pensize(10)
for i in range(12):
    pencolor(colors[i%2])
    forward(100)
    left(360/3)
    circle(40)

mainloop()    