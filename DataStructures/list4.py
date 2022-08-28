# Append Function

from audioop import reverse
from pickle import TRUE


fruits = []
fruits.append("Apple")
fruits.append("Banana")
fruits.append("Cherry")
fruits.append("Orange")
print(fruits)

fruits.insert(1, "Guava")
print(fruits)
fruits.insert(5, "Ananas")
print(fruits)

dry_fruits = ["Almond", "Cashew", "Walnut"]
fruits.extend(dry_fruits)
print(fruits)
#num = [1, 2, 3, 4, 5]
#fruits.extend(num)
#print(fruits)

# Sort function

#fruits.sort()
#print(fruits)

fruits.remove("Cherry")
print(fruits)

#fruits.reverse()
#print(fruits)

fruits.sort(reverse=True)
print(fruits)

l = fruits[::-1]
print(l) 