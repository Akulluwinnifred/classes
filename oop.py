#OOP-object oriented programming
#oop is a paradigm that advocates for developing software based on real world objects.
#classes vs objects
#principles of oop
#polymorphism
#abstraction
#inheritance
#encapsulation


#classes vs objects
#a class is a blueprint of an object(original copy of an object)
#e.g class car has objects such as benz, toyota, range rovers etc.
#class phone has objects such as itel, nokia, samsung , tecno etc.
#objects take on all features of a class but each object has different attributes

#an object is an instance of a class
#attributes of an animal are name, color, number of legs etc
#how to identify a class of an object,use a phase 'is a'
#e.g a cat 'is a' animal.therefore animal is a class while cat is an object animal.


#abstraction refers to ability to ignore other details and concentrate on the highest level of concentration
#it helps in simplifying complex systems by breaking them down into smaller manageable parts or components
#class name must me singular e.g car not cars

#Inheritance :here we have the concept of a parent and child
#parent class: provides common properties/methods which can be used by its child classes
#child class: inherits properties from parent class
#example : if you have a dog class and mammal class then dog will inherit from mammal because dogs are mammals.
#inheritance is the ability for an object to take on different attributes of a class e.g toyota wish belongs to class toyota and also class car

#polymorphism refers to the ability to take on different attributes of a class

#encapsulation is the ability to have what to share and what not to share











#write two dynamic functions that prompts a user to input name,age,email,gender and prints them out
# prompt to insert PAYE,NSSF and calculate net pay of an individual 




def  get_details(name,age,email,gender):
    name = input("Enter your name:")
    age = int(input("Enter your age:"))
    email = input("Enter your email address:")
    gender = input("Enter your gender: ")
    print(name,age,email,gender)
get_details("name","age","email","gender")
    

   
def employees(ppaye, nssf, salary):
    paye = (ppaye/100) * salary
    nSSF1 = (nssf/100) * salary
    netPay = salary - (paye + nSSF1)
    print(netPay)

ppaye = int(input('Please enter the PAYE percentage: '))
nssf = int(input('Please enter the NSSF percentage: '))
salary = 80000000

employees(ppaye, nssf, salary)



