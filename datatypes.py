#PPT 1
#Datatypes in python

x = 1000
y = 2000
x2 = -2334555
y2 = -9203
z = 12.50
s = 'fahim'
c = 'r'
print(x , type(x))
print(y , type(y))
print(x2 , type(x2))
print(y2 , type(y2))
print(z , type(z))
print(s , type(s))
print(c , type(c))
a = 0.111
print(a , type(a))
name = 'bruce wayne 01'
print(name , type(name))
color = 'yellow'
print(color , type(color))
institute = 'digipodium'
print(institute , type(institute))

#List in python

a = [5,10,15,20,25,30,35,40]
vals = [1,2.2,'python']
colors = ['red','green','yellow']
print(a)
print(vals)
print(colors)

#Tuples -> Tuples are immutable (unchangeable) and are used internally by mostly python.

a = (5,10,15,20,25,30,35,40)
vals = (1,2.2,'python')
colors = ('red','green','yellow')
print(a)
print(vals)
print(colors)

#Sets -> WE can peform set operations like union, intersection on two sets.

a = {5,10,15,20,25,30,35,40}
vals = {1,2.2,'python'}
colors = {'red','green','yellow'}
print(a)
print(vals)
print(colors)

#Dictionaries -> are optimized for retrieving data. We must know the key to retrieve the value.

car_info = {'brand' : 'Ford', 'model' : 'Mustang', 'year' : 1964}
print(car_info)