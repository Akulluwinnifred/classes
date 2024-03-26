#modula and object oriented
#this demonstrates how packages help organize and reuse code across different modules.
#a folder is a directory.
#a package is a directory where the modules are located
#a package must have a file named _init_.py because it is essential for telling python to that a directory is a package.


#Object oriented programming
#oop is a way of building software based on real world objects.
#in oop, we have classes and objects

#classes
#a class is a blueprint an object
#it defines the varialbles and methods of similar objects
#start with capital letters
#how to identify a class of an object, use 'is a'
#class names are always in singular e.g phone not phones
# example of a class
class Device:
    name = ""             
    edition = ""
    storage = ""  
    inches = ""
    version = ""
    color = ""
#in the above example, a class Book has been defined. A class acts as a blueprint for creating objects that share variables and methods
    def restart(self):
        return "My device is restarting"
#object
#an object is an instance of a class
#It is a specific example created from a class blueprint
#how to identify a class of an object, use 'is a'
#example of an object
hp = Device()
hp.name = "macbook air"
hp.storage = "32gb"
hp.edition = "macbook pro"
hp.inches = "16.9cm"
hp.version = "23H2"
hp.color = "Blue"


phone = Device()
phone.name = "Tecno"
phone.storage = "64gb"
phone.edition = "Android"
phone.color = "black"
#in the above example, I created objects of a class Laptop

#printing objects of a class
#f is a formatter which gives special attention to the curly bracket
print(f"{hp.name} has {hp.storage} of storage")
print(f"{hp.name} is {hp.color} in color")
print(f"{hp.name} has {hp.edition} installed")
print(f"{phone.name} is an {phone.edition} device")
print(f"{hp.restart()}")
#principles of oop:
#polymorphism
#inheritance
#abstraction
#encapsulation

#inheritance
#this involves creating child classes that inherit variables and methods from parent classes e.g iphone is belonging to a class Apple as well as a class phones

#abstraction
#it focuses on the essential details of an object and ignoring unnecessary details

#concept of encapsulation
#is the ability to have what to share and what not to share

#polymorphism
#allows objects to take on different attributes of a class
#e.g a move function might make a car drive