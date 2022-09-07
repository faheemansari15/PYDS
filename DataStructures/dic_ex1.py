info = ["Mistborn", "The Final Empire", "Brandon Sanderson", "tor.com", 2099, 2002]
info_dict = {
    "series" : "Mistborn",
    "title" : "The Final Empire",
    "author" : "Brandon Sanderson",
    "publisher" : "tor.com",
    "price" : 2099,
    "year" : 2002
    }

print(info_dict)
print(info_dict.keys())
print(info_dict.values()) 

my_dict = {"name" : "Jack", "age" : 23}
print(my_dict["name"])
print(my_dict.get("name"))
print(my_dict.get("age"))
#print(my_dict["address"])
#print(my_dict.get("address"))

# Update existing key
info_dict["price"] = 599
print(info_dict)

# Adding a new key value pair
info_dict["rating"] = 10
print(info_dict) 