dry_fruits = {"dates", "walnut", "cashew"}
fruits = {"mango", "apple", " guava"}

all_fruits = dry_fruits | fruits
print(all_fruits)

dis = dry_fruits.isdisjoint(fruits)
print(dis)

sub = dry_fruits.issubset(all_fruits)
print(sub)

sup = fruits.issuperset({"apple", "guava"})
print(sup)