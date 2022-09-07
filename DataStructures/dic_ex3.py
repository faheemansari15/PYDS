from pprint import pprint

movies = {}

# adding a single value
movies["Sholay"] = "2 friends fight with a dacoit"
movies["Inception"] = "No summary available"
print(movies)

# adding multiple values
movies.update(Ironman = "man buils a suit that is not iron",
Hulk = "story of a man that is not hulk",
Batman = "hero dresssed as a bat"
)

movies.pop("Sholay")

# Update
movies["Inception"] = "Dream within dream with recursion logic"

# Update 2
movies["Batman"] += " and fights crimes at nights"
#movies["Batman"] -= " crimes at nights"

print(movies)
pprint(movies) 