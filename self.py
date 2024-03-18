print("hello", "winnifred")
list=["apple","banana","cherry"]
print(list[0]) #accessing the first element of list
list.append("blackberry")#adding an item to the end of a list
print(list)
list.insert(1,"passion fruits")#inserting an item to a specified position
print(list)
list.remove("banana" )#removing an item from the list
print(list)
# Initialize a counter variable
counter = 0

# Define the condition for the while loop
while counter < 5:
    print("Counter:", counter)
    counter += 1  # Increment the counter variable

print("Loop finished")
seats = 5
while seats > 0:
    print("take your seat")
    seats -= 1

print("loop finished")
i = 3
for i in range(3):
    print("true")

print("false")

mydetails = {"name":"Akullu","age":24,"country":"England"}
print(mydetails)
print(mydetails.keys())
print(mydetails.values())

print("my name is Akullu Winnifred")
print("Hello" + "Winnifred")

list = ["winnifred","Vanessa","patrica",["Esther","Ritah",["Emmanuel",["Isaiah"]]]]
print(list[3][2][0])
print(list[-1][-3])