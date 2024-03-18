#datatypes in python
#categorization of data types
#numeric
#string
#sequence
#mapping
#boolean
#set


#numeric:we have integers(int),float and complex numbers(complex)
num1=10
print(num1, "is of a type",type(num1))
num2=6.0
print(num2, "is of a type",type(num2))
num3 = 1+2j
print(num3, "is of a type",type(num3))


#strings
#A string is a group of characters e.g(name="winnifred")
#the value of a string is identified using double or single quotes(""'')
name="winnifred"
print(name, "is of a type",type(name))
#semantics is the meaning of what you have written
#typecasting is the conversion of data types
num6 = "20"
print(num6,"is of a type",type(num6))
#example of type casting
numx = int(num6)#conversion of num6 to an integer and storing in numx
print(numx,"is of a type",type(numx))
numy=float(numx)
print(numy,"is of a type",type(numy))
numz=str(numy)
print(numz,"is of a type",type(numz))

#sequence
#under sequence we have lists,range and tuples
#lists is a variable that can store more than one value 
#however we can have an empty list meaning we can store values later
mylist=[]
mylist.append("Akullu")
print(mylist)
mylist.append(15)
print(mylist)
#append is a specialized command in python to add values to a list
#print is a specialized command in python used to output values on a computer screen
languages=["python", "javascript","C++","java","C","C#","swift","ruby","cobol"]
print(languages[5])
print(languages[0])
print(languages[1])
print(languages[7],languages[3])
print(languages[-1])

country=["uganda","kenya","tanzania",["Egypt","somalia",["sudan",["burundi",["Togo"],["Benin"]]]]]
print(country[3][2][0])
print(country[-1][-1][-1][-1])
print(country[3][2][1][0])
print(country[-1][-1][-1][-2])

fruits = ("apples","mangoes","oranges",["pawpaws","pears"])
print(fruits[1])
print(fruits[-1][-2])
print(fruits[-1][-1])

#A list is a mutable datatype because it can be manipulated after it has been created
#A tuple is immutable meaning it can not be manipulated once created
#tuples can be typecasted thus you can change a list into a tuple but you cant change a tuple into a list


#mapping
person = {"name":"winnifred","age": 6,"country":"Uganda","height":171}
#A variable whose value is enclosed in a curly bracket is called a dictionary
print(person)
print(name)
print (person.keys())
print (person.values())

#A set is an unordered collection of unique values
student_id = {120,144,177,488,788,788}
print(student_id)
print(student_id)







