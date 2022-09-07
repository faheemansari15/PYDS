def area():    
    l = int(input("enter the length"))
    b = int(input("enter the width"))
    area = l * b
    return area # l * b

print("area = ", area())

ans = area()
print("area", ans)

ans = area() + area() - area()
print("total area = ", ans)


def minmax():
    x = [2, 4, 6, 8, 10, 12]
    return min(x), max(x) #returning more than 1 value

values = minmax()

a, b = minmax()

print(minmax())
print(values)
print(a, b) 