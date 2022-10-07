# variable arguments - args
# keywords arguments - kwargs

def total(*values):
    t = 0
    for i in values:
        if isinstance(i, (int, float)):
            t += i
    return t

o = total(1, 2, 3, 4)
print(o)

o = total()
print(o)

o = total(2, 3, 4, 5, 6, 7)
print(o)

o = total(3, 5, 7, "A", 8, "b", 10)
print(o) 