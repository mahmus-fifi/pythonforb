"""
Functions are used to group blocks of code together. They can return a value and take more than one input.
How functions work are hidden from the user. So you don't need to know how a function was created to know how to use it.
Similar to how you don't need to know the Gas compression ration of a car to know how to drive on

"""
# python built in functions 
# len() function

lst = ["Today is a good day for science"]
length_of_lst = len(lst) # we need to feed the method with data. that data is called an argument pr parameter
print(f'The length of the list is {length_of_lst}')

# len() returns an integer 
number = 5
add_5 = length_of_lst + number
print('we took %d and added to it, now we have %d' %(number,add_5))

# let's create our own functions 

# this is an empty function that dosen't do anything yet, thats why we added the pass keyword 
def dummyFunction():
    pass

# function that does something  
def sayHello(greeting):
    print(greeting)
# you have to call the function to use it 
sayHello("Hi there champ!")

def IDontArgue():
    print('I am a cool and calm person! I got Chill')
    
# calling the function 
IDontArgue()

# creating a function that returns a result 
def ReturnOftheTerminator():
    print('Guess who is back')
    return 'Am Back!'
# calling the function 
ReturnOftheTerminator()

# printing the function
print(ReturnOftheTerminator())

# calculate Area
PI = 3.14
radius = r = 2.6 
Area = PI * (r**2)
print('Area of the circle is: %d sq meters.' %Area)

def Area(radius):
    PI = 3.14
    area = PI * (radius ** 2)
    print(f'the area of the Circle is: {area} sq meters')
# calling the area function 
Area(12.5)
Area(12.33)
Area(3.21)

def AreaReturn(radius):
    """Calculates the area of a Circle"""
    PI = 3.14
    area = PI * (radius ** 2)
    return area
# calling the area function 
result = AreaReturn(0.23) * 8
print(f'The result of the calculation is: {result:.2f}')

# function scope
# global variable (accessed anywhere)
y = 33

def printNum():
    x = 29 # local Variable (accessed only in the function)
    print(y)
printNum()
#print(x) # error cause we cannot reach x 

# method that multiplies two numbers 
def MultiplyTwoNumbers(firstnum, secondnum):
    print("***************************")
    print("Welcome to the number multiplier program")
    # ask user to enter the first number
    firstnum = float(input("Enter the first number: "))
    # ask the user to enter the second number
    secondnum = float(input("Enter the second number: "))
    # store the result of multiplying first number by second number
    result = firstnum * secondnum # return firstnum * secondnum
    print(f'Multiplying {firstnum} by {secondnum} we get :{result:.3f}')
    return result

#MultiplyTwoNumbers(1,3)
keepit100 = 100
solution1 = MultiplyTwoNumbers(0,0) * keepit100
print(type(solution1))
print('Results for solution1 = %d' %solution1)










    




