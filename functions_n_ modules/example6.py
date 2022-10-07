'''lambda a,b:a+b

adder = lambda a,b:a+b
print(adder(69,225))

def exp(power):
    return lambda l : [a**power for a in l]
four = exp(4)
four([2, 4, 6, 8, 10])'''

x = [2, 3, 4, 5, 10, 20, 40]
o = list(map(lambda i:i**2, x))
print(o) 

x5 = list(map(lambda i:i-5, x))
print(x5) 

y = [1, 4, 6, 7, 8, 9,]

xy = list(map(lambda a,b:a+b, x, y))
print(xy) 

y3 = list(filter(lambda i: i>3, x))
print(y3) 

name = ["Raj Singh", "Ram Singh", "Roma Verma", "Neha Jha", "Atul Singh"]

name_singh = list(filter(lambda i: i.endswith("Singh"), name))
print(name_singh) 

name_s = list(filter(lambda i: i.startswith("R"), name))
print(name_s) 

print(range(1, 10)) # "range" -> Special type function which are the generators 