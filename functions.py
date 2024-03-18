#a function is a named block of code(group of statements) and performs a specific task
#functions are the building blocks of programming languages e.g


def myfunction():
    num1, num2 = 20, 40
    print(num1 + num2)
myfunction()

#there are two types of functions
#static functions
#dynamic functions

def condition():
    number = 10 #function definition is whatever is in the body of a function name
    if number > 0:
        print("number is positive")
    print("the if statement is easy")



#below is when it is removed from the above function
number = 10
if number > 0:
   print("number is positive")


#a function is called anywhere within the file
#calling a function is called INVOKE
condition()



def mycondition():
    number = -10
    if number > 0:
        print("positive number")
    else:
        print("the number is negative")
    print("this statement is not related to if or else but in the same function")


mycondition()


