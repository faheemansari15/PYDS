# Create a list with 10 numeric values from user
# then find the min, max, total, avg, median

import statistics as stat

x = []
for i in range(1, 11):
    val = int(input(f'Enter value {i}: '))
    x.append(val)

print("The list")
for i in x:
    print(i, end=" ")
    # print(" ", join(x))

print("\nMinimum value: ", min(x))
print("Maximum value: ", max(x))
print("Sum of values: ", sum(x))   
print("Average of values: ", stat.mean(x))
print("Median of values: ", stat.median(x)) 