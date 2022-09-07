# definition function
def area():
    l = int(input("enter the length"))
    b = int(input("enter the width"))
    area = l * b
    print(f"{l} x {b} = {area}")

# calling function/use
area()

# function definition
def prime():
    x = []
    for num in range(2, 20):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            x.append(num)
            print(num, end=" ")
# function calling/use
prime()

# find length of strings with adding two (len) functions 
ans = len("Hello") + len("Faheem")
print(ans) 