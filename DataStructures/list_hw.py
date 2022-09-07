# wap to create a list from user of n elements, if the user enters a duplicate
# value dont add it to list and warn the user about their mistake

# wap to create a list and then replace all value greater than 5 by 0

# wap to create a list that contains 5 small sublist of 3 items each (nested list)
# take the input from user to create this nested list

x = []
for i in range(20):
    x.append(i)
    if i > 5:
        x.remove(i, 0)
    print(i)