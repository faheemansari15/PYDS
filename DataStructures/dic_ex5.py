# create a contacts dictionary, where the user can search for a person name and if the name exists, it display
# the phone number
# else, the user should be provided a choice to add the phone number of that person
# also the user can also choose to list all person and numbers

cont = {
    "Altamash" : 9898898998,
    "Kausar" : 9877899879,
    "Faheem" : 9044512015,
    "Ansari" : 7887788798
}

print(cont)

'''user = input("Enter the person name")

if user in cont:
    print(cont[user]) 
else:
    print("name does not exists, would you like add the person's number")
    
    print(cont.update())'''

while True:
    print("# Options")
    print("1. Search Person")
    print("2. View all")
    print("3. Exit")

    ans = input("Enter a number")
    if ans == "1":
        name = input("Enter the person's name")
        if name in cont:
            print(f"{name} => {cont[name]}")
        else:
            print(f"Npt found, would youn like to add the {name}'s number")
            number = input(f" enter number for {name} =")
            cont[name] = number
            print("Details added")
    elif ans == "2":
        for name, number in cont.items():
            print(f"{name} => {number}")
    elif ans == "3":
        print("Bye")
        break
    else:
        print("wrong input")                    