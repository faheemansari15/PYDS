# create a list of 10 numbers and then
# genarate a list which holds the square vals of original list
# genarate a list which holds the cubes vals of original list

x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

x2 = []
for i in x:
    sqr = i ** 2
    x2.append(sqr)
print("List: ", x)
print("List of squars: ", x2)    


x3 = []
for i in x:
    cube = i ** 3
    x3.append(cube)
print("List: ", x)
print("List of cubes: ", x3) 