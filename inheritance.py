class Animal:
    name = ""
    def eat(self):
        print("i can eat")


#dog is the child/derived/sub class
#Animal is the parent class
class Dog(Animal):
    def display(self):
        print(f"my name is {self.name}")

gshepherd =  Dog()
gshepherd.name = "police"
print(gshepherd.name)
print(gshepherd.display())
print(gshepherd.eat())



#create three super classes with corresponding 2 sub classes of each and create 3 objects from them




# Superclass 1
class Animal:
    def __init__(self, species):
        self.species = species

# Subclasses of Animal
class Mammal(Animal):
    def __init__(self, species, fur_color):
        super().__init__(species)
        self.fur_color = fur_color

class Reptile(Animal):
    def __init__(self, species, scale_type):
        super().__init__(species)
        self.scale_type = scale_type

dog = Mammal("Dog", "Brown")
snake = Reptile("Snake", "Smooth")
# Superclass 2
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

# Subclasses of Vehicle
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

class Motorcycle(Vehicle):
    def __init__(self, brand, type):
        super().__init__(brand)
        self.type = type


toyota = Car("Toyota", "Corolla")
harley = Motorcycle("Harley-Davidson", "Cruiser")

# Superclass 3
class Furniture:
    def __init__(self, material):
        self.material = material

# Subclasses of Furniture
class Chair(Furniture):
    def __init__(self, material, style):
        super().__init__(material)
        self.style = style

class Table(Furniture):
    def __init__(self, material, shape):
        super().__init__(material)
        self.shape = shape

# Creating objects

wooden_chair = Chair("Wood", "Modern")
glass_table = Table("Glass", "Rectangular")
