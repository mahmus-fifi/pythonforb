# handling errors in python 
# Error Types 
# Syntax Error,ValueError, NameError, TypeError, DividebyZero 

# Example 0 Syntax error
#Print("Hello world") # print should be print()
if 3 > 5: # forgetting the : or not indenting will create an error 
    print(3> 5)
# Example 1 NameError
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
    
    
"""Ways to Handle Errors (Exceptions)"""
# local and global variables 
age = 24
power_up_max = 10 

# let's printout the global in our program 
#print(f'global variables in the scope: {globals()}')
name = 'mahmus'
user_name = 'baby'
#print(name) # name is not defined

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

user = 12
if not type(user) is int:
    raise TypeError('Only numbers are allowed')


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







    


