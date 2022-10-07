def default_func(a=50, b=100):
    return a + b
print(default_func())
default_func() 

print(default_func(a=200))

print(default_func(b=300)) 

def triangle_area(b, h=1):
    return .5 * b * h

#print(triangle_area()) Error!
print(triangle_area(10))
print(triangle_area(8, 2))
print(triangle_area(b=5))
print(triangle_area(b=5, h=15))

def read(filepath=None):
    if filepath:
        with open(filepath) as f:
            return f.read()
    else:
        return "Please provide a filepath"

print(read("g1.py"))
print(read())                