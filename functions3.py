
#functions are self contained block of codes
#values put in the paranthesis are called parameters
def add(a,b):
    ans = a + b
    print(ans)

#a global variable can be accessed in the function below
total = 10
#values put in the paranthesis are called parameters
def add1(a,b):
    ans = a + b + total
    print(ans)
add1(2,4)