#loops and conditions
#loops tells a computer to do something repeatedly 
#there are two types of loops : while loop, for loop.
#for loop e.g
for i in range(5):
    print("Hello")  #this will display Hello five times


for i in range(1,20):
    if i % 2 ==0:
        print(i)


digits = [2,3,4,5,6,7]
for item in digits:
    print(item)
else:
    print("out of range")

#while loops
seats = 10
while seats  > 0:
    print("sell tickets")
    seats -= 1
else:
    print("no more tickets")


info = { "name":"Winnifred", "age":30, "color":"chocolate", "country":"Nigeria" }
for keys,values in info.items(  ):
    print(keys,values)




#else,elif,and else e.g
age = 67
if age < 18:
   print("You are a minor.")
elif age == 18:
   print("transition stage")
else:
   print("You are an adult.")


#functions is a named block of code
#functions is a building block of programming languages
#there are two types of functions: static and dynamic functions
#static function has no arguments e.g
def mult():
    num1,num2 = 20,10
    mult = num1 * num2
    print(mult)
mult()


#dynamic functions can take on any arguments since they have defined parameters
def discount(price,discount_percentage):
    discount = (discount_percentage / 100) * price
    print(discount)
discount(20000,20)



#functions can also use global values e.g
total = 35
def sum(a,b):
    sum = a + b + total
    print(sum)
sum(2,3)


#return is the last statement to be executed in a function e.g
#In this case the print statement will not be executed
def mult():
    num1,num2 = 20,10
    mult = num1 * num2
    return(mult)
    print(mult)
mult()


#we can create functions which share one anothers values e.g
def rest_bill(meal_cost, tip):
    ftip = (tip/100) * meal_cost
    return ftip
rest_bill(30000, 15)


def bill_amount(meal_cost, ftip):
    total_bill = meal_cost + ftip
    return total_bill
bill_amount(30000, 4500)



def net_change():
    cash = 100000
    act_bill_amount = bill_amount(30000, 4500)
    net_change = cash - act_bill_amount
    print(net_change)
net_change()









