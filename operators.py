#An operator is a special xter that tells a computer what to do with the value
name = "winnifred"
# Operator symbols and their meaning
#Arithmetic operators(+,-,*,/,//) perform arithmetic operations on numbers.
num1 = 101
num2 = 200
sum = num1 + num2
print(sum)

#substruction
sub = num1 - num2
print(sub)

#multiplication
mul = num1 * num2
print(mul)

#division
div =  num1 / num2
print(div)

#floor division 
floordiv = num1 // num2
print(floordiv)

#exponential/power(**)
print(num1**2)
print(4**3)

#modulo  (%) returns the remainder of one number divided by another
print(num1 % num2)

#Assignment operators

#equal sign
num3 = num1 + num2

#addition assignment
num1 += 2 #num1 = num1 + 2
print(num1)

#subtraction assignment
num1 -= 2
print(num1)

#multiplication assignment
num1 *= 2
print(num1)

#division assigment
num1 /= 2
print(num1)
#exponential assignment
num1 **= 2
print(num1)

#modulus assignment
num1 %= 2
print(num1)


#comparison operators,compares two variables
#boolean datatypes(true/false,yes/no,0/1)
comp1 = 100
comp2 = "winnifred"
print(comp1 == comp2)   #False because it is comparing a number to string. 
#two equal sign assignment operators equals a comparison operator
#you start with ! = for not equal to
print(comp1 != comp2) 

#greater than/less than
print(comp1 < num1) 
print(comp1 > num1)

#greater/less than equal to
print(10 <= 20)
print(10 >= 20)

#logical and
print(True and True)
print(True and False)

#logical or
print(True or False)

#logical not
print(not True)

#membership operators (in/not in)
mylist = [10, 20, 30, 40, 50]
print(10 in mylist)
print(100 in mylist)
print(100 not in mylist)

#identity operators
mylist2 = [10, 20, 30, 40, 50]
print(mylist is not mylist2)
print(mylist is mylist2)

#simple assignment,read about bitwise operators
#bitwise operators


#a statement that evaluates to a value is called an expression
#a value in programming is called an operand
#operators acts on operands.
#an opperand is what an operator acts upon










