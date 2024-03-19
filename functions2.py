def add():
    num1,num2 = 10,20
    sum = num1 + num2
    print(sum)
add()


#creating a dynamic function
def add1(num1,num2):
    sum = num1 + num2
    print(sum)
add1(100,50)
add1(200,500)


def sub(num1,num2):
    sub = num1 - num2
    print(sub)
sub(100,50)
sub(200,500)


def modulo(num1,num2):
    mod = num1 % num2
    print(mod)
modulo(100,50)
modulo(200,500)


def mult(num1,num2):
    mult = num1 * num2
    print(mult)
mult(100,50)
mult(200,500)

def exp(num1,num2):
    exp = num1 ** num2
    print(exp)
exp(4,2)

#functions can take multiple datatypes e.g 
def multidata(num1,num2,name,flt):
    print(num1)
    print(num2)
    print(name)
    print(flt)
multidata(20,30,"winnifred",3.67)


def multidata1(num1,district,name,flt):
    print(num1)
    print(district)
    print(name)
    print(flt)
multidata(20,"mukono","winnifred",3.67)


def hack(name,yob,district):
    print(name)
    print(yob)
    print(district)
    currentyear = 2024
    age = currentyear - yob
    print(name,"is",age)
hack("winnifred",1999,"oyam")




