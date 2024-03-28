
class Food:
    name = ""
    def eat(self):
        return "I am edible"


class Fruit(Food):
    def display(self):
        print("I am a", self.name)


class Vegetable(Food):
    def vtype(self):
        print("this is a", self.name)

carrot = Vegetable()
carrot.name = "Bobo"
print(carrot.name)
print(carrot.vtype())
print(carrot.eat())

apple = Fruit()
apple.name = "red"
print(apple.name)
print(apple.display())
print(apple.eat())


brocolli = Vegetable()
brocolli.name = "Bobo"
print(brocolli.name)
print(brocolli.vtype())
print(brocolli.eat())



class ElectronicDevice:
    name = ""
    def restart(self):
        return "My device is restarting..."


class Laptop(ElectronicDevice):
    def myelectronics(self):
        print(self.name + " is an electronic device.")


class Smartphone(ElectronicDevice):
    def myphone(self):
        print(self.name + " is a smartphone.")


iphone = Smartphone()
iphone.name = "iPhone XS Max"
print(iphone.myphone())
print(iphone.restart())
        

macbook = Laptop()
macbook.name = "MacBook Pro"
print(macbook.myelectronics())
print(macbook.restart())

hp = Laptop()
hp.name = "MacBook Pro"
print(hp.myelectronics())
print(hp.restart())


class Clothing:
    name = ""
    def  wear(self):
        return self.name + " is being worn."

class Shirt(Clothing):
    def myshirt(self):
        print("this is my",self.name)

class Pants(Clothing):
    def mypants(self):
        print("this is my",self.name)
        

tshirt = Shirt()
tshirt.name = "T-Shirt"
print(tshirt.wear())
tshirt.myshirt()


jeans = Pants()
jeans.name = "Dior"
print(jeans.wear())
jeans.mypants()


gentle = Pants()
gentle.name = "gentle_trouser"
print(gentle.wear())
gentle.mypants()