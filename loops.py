#loops and conditions
#loops is used to tell a computer to repeatedly do something till the condition is met

#a loop is a way of writing instructions to a computer until a certain condition is met
#below is an iteration of values in a list of numbers
def loop1():
    list = [10, 20, 30, 40, 50]
    for item in list:
        print(item)
loop1()
def loop2():
    for i in range(10):
        print(i)
loop2()
#item = 1
for item in range(1,10):#1 represents the start of the list
    print(item)
for i in range(2,3):
    print(i)
#range is a keyword in python.
for i in range(4,20,4):
    print(i)
#loops are very expensive in terms of memory
#two types of loops,for and while loops.

for i in range(1,20):
    if  i % 2==0:
        print(i)

#below is a block of code(a collection of related statements) identified by indentation and colons
for i in range(1,20):
    if  i % 2==1:
        print(i)


digits = [23,67,50,70,89]
for i in digits:
    print(i)
else:
    print("no items left")


#while loop 

lakes = { "name":"L.victoria", "width":30, "color":"blue", "location":"Africa" }
for keys,values in lakes.items(  ):
    print(keys,values)
for items in lakes:
    print(items)

