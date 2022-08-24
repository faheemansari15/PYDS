#chr
x = chr(65)
print(x)

x = chr(2365)
print(x)

x = (12365)
print(x)


#ord
y = ord('A')
print(y)

y = ord('a')
print(y)

y = ord('{')
print(y)


#len
print(len('amazing'))
print(len("Fahim"))
size = len("hope")
print(size)


#str
x = 65



a = 'apple'
b = 'juice'
ab = a+b
print(ab)

w1 = 'this'
w2 = 'is'
w3 = 'fahim'
out = w1 + w2 + w3
print(out)

out = w1 + ' ' + w2 + ' ' + w3
print(out)


#Duplication
word = 'Hello'
print(word * 5)

print('_' * 150)

#Pattern
'''for i in range(1,6):
    print(i * ' * ')

for i in range(1,-6):
    print(i * ' * ')

for i in range(-1,6):
    print(i * ' * ')

for i in range(-1,-6):
    print(i * ' * ')   


for i in range(6,0,-1):
    print(i * ' * ')'''          



for i in range(1,6):
    print((i * ' l ').rjust(15))



for i in range(1,15,5):
    print((i * ' T ').center(30))


for i in range(1,15,2):
    print(i * ' * ').center(30)
    print(i * ' 0 ').center(30) 