from turtle import *

'''speed("slowest")
forward(100)
left(90)

mainloop()

speed("fastest")
forward(100)
left(72)
forward(100)
left(72)
forward(100)
left(72)
forward(100)
left(72)
forward(100)
left(72)

mainloop()

speed("fastest")
for i in range(8):
    forward(100)
    left(360/8)
mainloop()

sides = int(input("How many sides do you want"))
distance = int(input("How far do you want to go?"))'''
sides = 8
distance = 50
fillcolor("black")
begin_fill()

for i in range(sides):
    forward(distance)
    left(360/sides)
end_fill()
mainloop()    