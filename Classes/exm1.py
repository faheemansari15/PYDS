class Cat:
    # attributes, fields, class members, properties
    color = "black"
    breed = "persian"
    age = 2

    # methods/functions
    def eat(self):
        print("Cat is eating")

    def play(self):
        print("Cat is playing")

    def description(self):
        print(f"Cat is {self.age} years old")
        print(f"Cat is {self.color} in color")
        print(f"Cat is {self.breed} breed")

# object                 
tom = Cat() # to call the constructor the class

tom.eat()
tom.play()
tom.description() 

tom.age = 3
tom.breed = "street walk"
tom.color = "grey"

print("age", tom.age)
print("color", tom.color)
print("breed", tom.breed) 