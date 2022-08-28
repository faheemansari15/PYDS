# Count Function

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50]
a = x.count(1)
print(a)

print(x.count(100))

# Index Function

movies = ["Ghostbusters: Afterlife", "Spider-Man: No way home", "Shang-chi", "The last duel", "Venom: Let there be carnage"]
i = movies.index("Venom: Let there be carnage")
print(i)
print(movies.index("Shang-chi")) 

# Copy Function

fruits = ["Cherry", "Guava", "Apple", "Banana"]
dup_fruits = fruits.copy()
print(dup_fruits)

# Append function

val = fruits
val.append("Ananas")
print(val)
print(fruits)

fruits.append("Dates")
print(fruits)

# Clear Function

fruits.clear()
print(fruits)

# Pop Function

fruits = ["Cherry", "Guava", "Apple", "Banana"]

# By list.pop() method

v = fruits.pop()
print(v)
print(fruits)

# By list.pop(index) method

v1 = fruits.pop(2)
print(v1)
print(fruits)
print(fruits.pop(0))
print(fruits) 