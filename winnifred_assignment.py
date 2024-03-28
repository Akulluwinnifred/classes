def tests(test1, test2):
    #a function tests is defined and  called to check if the two parameters are equal or not.
    if test1 == test2:
        # If they are equal it displays the value of test1
        return test1
    else:
        #if they are not equal,then it displays the value of test2
        return test2
#this prompts the user to input the values of test1 and test2

test2 = int(input('Please enter Marks for test two: '))
test1 = int(input('Please enter Marks for test one: '))
'''
the eror was because test1 was not defined
I have defined the value of test1 as below
test1 = int(input('Please enter Marks for test one: '))
prompting the user to input the values of test1 and test2 as an integer
creating two dynamic functions that share values
creating a function whose values can be used by another function
the function calculates the final coursework marks based on tests and coursework marks
'''
def courseWrk(cswork):
    #Sharing the arguments of the parameters of the fuction tests to calculate the testsMark
    testsMark = tests(test1,test2)
    #This will calculate and hold the value of the average of  the marks testsMark and cswork
    avgtestsCswork = (cswork + testsMark)/2
    #this calculates the final coursework mark interms of percentage
    fnltestsCswork = avgtestsCswork * (40/100)
    #displays the line of dots
    print('..............................')
    #This  will display the final score after calculating the percentage of avgtestsCswork which is the value of fnltestsCswork
    print('your final coursework marks is: ', fnltestsCswork)
    print('..............................')
#This prompts the user to assign the variable cswork a value which is an integer
cswork = int(input('Please enter your course work Marks: '))
#Invoking the dynamic function  with cswork parameter
courseWrk(cswork)