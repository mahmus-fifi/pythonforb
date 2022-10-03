# handling errors in python 
# Error Types 
# Syntax Error,ValueError, NameError, TypeError, DividebyZero, LogicalErrors 
# A syntax Error is a typographical error, it happens when a programmer spells a variable 
# or Built-in type wrong or fails to add a comma or colon where necessary 
# e.g 
"""
for i in range
    print i
color ':' after range was forgotten 

this will throw a syntax error and python will try to make a suggestion to fix it 

also using Print() with capital 'P' instead of print()

forgetting to close a parenthesis will also show an error eg print( closing ')' not used 
"""
# Indentation Error
"""
# An Indentation Error occurs when a programmer uses the wrong indent, especially 
# when using loops etc 
if 3 > 5: # forgetting the : or not indenting will create an error 
    print(3> 5)
"""

"""Manual Ways to Handle Errors (Exceptions) using data integrity checks"""
# Example 1 
# checking input type
# local and global variables
def DataChecker(): 
    num = int(input('Enter a number: '))
    # cast the input to a number using int(input("Enter a number: "))
    if type(num) == int:
        print(f'Data type of the value {num} is integer')
    elif type(num) != int:
        print('%s is not an integer' %num)
    elif type(num) == float:
        print('You entered a floating point number, enter float only')
    if type(num) == str:
        print('You entered a strings value, convert to integer.')
# running the function
#DataChecker('Hi') # typeError  
DataChecker()


# Example 2 NameError
#print(num) # name is not defined
# using try except block 
try:
    print(num)
except:
    print('num is not defined, an error happened, define num')
# add other exception types 
try:
    print(stuff)
except NameError:
    print('Cant find a variable called stuff')
except:
    print('other error exists')
    

"""
# program will loop until right input is set 
done = True 
while done:
    try:
        user_input = int(input("Please enter a number: "))
        break # exit the program when user enters an integer 
    except (ValueError, NameError, TypeError):
        print('Enter numbers only, try again!')
        
    finally:
        print('code executed')
"""


# using a try catch block 
def firstError():
    print()
    try:
        num = int(input("Enter the first number: "))
    except ValueError:
        print('You can only input numbers, not text') 
    else:
        print(f'you entered {num} as the first number')
    try:
        num2 = int(input("Enter the second number: "))
    except ValueError:
        print('You can only input numbers, not text') 
    else:
        print(f'you entered {num2} as the second number')
    try: 
        # divide the first input by the second input 
        result = num/num2
        print('Result: %s'%result)
    except ZeroDivisionError:
        print("Divide by Zero Encountered")
    finally:
        print('code completed sucessfully')   
firstError()







    


