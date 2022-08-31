# Create a list will 10 vlues entered by user and the sort the values
x = []
for i in range(10):
    val = input(f'Enter value {i+1}: ')
    x.append(val)

print("The list")
x.sort()
for val in x:
    print(val, end=" ")
    # print(" ", join(x))
