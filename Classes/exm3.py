class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def info(self):
        print("FRUIT")
        print(f"{self.name}")
        print(f"{self.color}")

class Mango(Fruit):
    def __init__(self, name, color, taste, size):
        super().__init__(name. color)
        self.taste = taste
        self.taste = size

f = Fruit        
