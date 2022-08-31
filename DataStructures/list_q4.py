# create a list of n items
# generate a list of only even number from exixting list
# generate a list of only odd number from exixting list
# generate a list of only number > n from exixting list, where n can be any value

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

xe = []
for i in x:
    if i % 2 == 0:
        xe.append(i)
print(x)
print(xe)        

xo = []
for i in x:
    if i % 2 != 0:
        xo.append(i)
print(x)
print(xo)        

xg5 = []
for num in x:
    if num > 5:
        xg5.append(num)
print(x)
print(xg5) 

n = int(input("Enter a number"))
xgn = []
for i in x:
    if i > n:
        xgn.append(i)
print(x)
print(xgn) 