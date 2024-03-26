#defining an object in python
class Animal:
    color = ""
    size = ""
    gender = ""
    name = ""
    species = ""
    sound = ""
    age = 0

#A method is the function of a class and statement within that method is called a behaviour.

    def feed(self): #this is a method of animal class feed
        
        return "by chewing"

#creating objects of a class animal
cat = Animal()
cat.name = "Whiskers"
cat.color = "chocolate"
cat.size = "medium"
cat.gender = "male"
cat.species = "feline"
cat.sound = "Meow!"
cat.age = 17

#accessing obects
print(f"{cat.name} is {cat.age} years old") 
print(cat.name +  " does " + cat.sound )
print(f"{cat.name} is {cat.size} and {cat.color} ")
print(f"{cat.name} is of {cat.species} species ")
print(f"{cat.name} is {cat.gender} and {cat.color} ")
print(f"{cat.feed()}" )  


dog = Animal()
dog.name = "Buddy"
dog.color = "brown"
dog.size = "large"
dog.gender = "male"
dog.species = "canine"
dog.sound = "Woof! Woof!"
dog.age = 3




cow = Animal()
cow.name = "Daisy"
cow.color = "white"
cow.size = "large"
cow.gender = "female"
cow.species = "bovidae"
cow.sound = "moow"
cow.age = 40


sheep = Animal()
sheep.name = "Bobo"
sheep.color = "black"
sheep.size = "small"
sheep.gender = "male"
sheep.species = "ovata"
sheep.sound = "baa baa"
sheep.age = 3