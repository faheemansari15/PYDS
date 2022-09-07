# Create a prime numbers list upto size n
# 2, 3, 5, 7, 11, 13,......

x = []
for num in range(2, 20):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        x.append(num)
        print(num, end=" ")
#for p in x:
    #print(p, end=" ")        