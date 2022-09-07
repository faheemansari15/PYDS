def word_counter(s):
    words = s.split()
    return len(words)

def area(l,b):
    return l * b

def circumstance(r):
    return 2 * 3.14 * r        

wcount = word_counter("Faheem Ansari")
print(wcount)
print(word_counter("This is Faheem"))
print(word_counter("My full name is Faheem Ansari"))
print(word_counter("Aur kaise hein aap sab"))
print(word_counter("Chaliye shuru karte hein"))    

# call area and circumstances

# 1. direct
print(area(4,4))
print(circumstance(4)) 

# 2. user input
a = int(input("enter the length"))
b = int(input("enter the width"))
c = area(a,b)
print("area = ", c) 

# 3. shorter user input
c = area(int(input("lentgh:")), int(input("width:")))
print("area =", c) 