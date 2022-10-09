"""
Functions are used to group blocks of code together. They can return a value and take more than one input.
How functions work are hidden from the user. So you don't need to know how a function was created to know how to use it.
Similar to how you don't need to know the Gas compression ration of a car to know how to drive on
"""
# working with functions 
# len() str()
lst = ["Today is a good day for coding!"]
length_of_list = len(lst)
#print(length_of_list)
#print(f'The length of the list is: {length_of_list}')
number = 5
add_5 = length_of_list + number
#print('we took %d and added to it, now we have %d'%(number, add_5))
# creating our own functions 
def dummyFunction():
    pass
# calling a function 
dummyFunction()
# function that does something  
def sayHello(greeting):
    print(greeting)
sayHello('Hi')

def IDontArgue():
    print('I am a cool person!')
IDontArgue()

# function that returns a result 
def ReturnOfTheTerminator():
    print('Guess whose back')
    return 'Am Back!'
print(ReturnOfTheTerminator())

# Calculate the Area of a Circle 
PI = 3.14
CONSTANT = 2
radius = r = 2.6
Area = PI * (r ** CONSTANT)
print('Area of the Circle is: %d square meters' %Area)

# using a function to calculate area 
def Area(radius):
    PI = 3.14
    area = PI * (radius **2)
    print(f'Area of the circle is: {area:.2f} sq meters')
    
Area(0.23)
Area(2.22)
Area(12.45)

# using Area and a return method 
def AreaReturn(radius):
    """Calculates the Area of a Circle"""
    PI = 3.14
    area = PI * (radius ** 2 * number)
    return area
result = AreaReturn(0.23) * 100
print(f'The Area is: {result}')

def printNum():
    x = 29
    print(x)
       
printNum()
#print(x)
# program that multiplies two numbers 
def MultiplyTwoNumbers(firstnum, secondnum):
    print('*****************************')
    print('Welcome to the number multiplier program')
    # ask user to enter the first number 
    firstnum = float(input("Enter the firstnumber: "))
    # ask user to enter the second number 
    secondnum = float(input("Enter the second number: "))
    # storing the value of the multiplication
    result = firstnum * secondnum
    print(f'Multiplying {firstnum} by {secondnum} we get: {result:.3f}')
    return result
# calling the multiply method 
#MultiplyTwoNumbers(0, 0)
#MultiplyTwoNumbers()
keepit100 = 100
solution1 = MultiplyTwoNumbers(0,0) * 100
print('Results for solution 1 = %d' %solution1)

















    



























    












