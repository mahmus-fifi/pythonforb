
# working with lambda expression 
# created by Mahmud Shuaib
# 1st October 2022
"""
All functions have a name, if you want to create a nameless function (anonymus) function,
you can use a lambda function.

Lambda functions are used when anonymus functions are required for a short time in a program
"""
def Name(name):
    return name
name = Name("Mahmus")
print(f'hi, my name is {name}!')

# using lambda 
# syntax 
# lambda arguments: expression
"""A function that concatenetes a string """ 
greeting = lambda name : "hi " +name
print(greeting('Mahmus'))


# a function that raises the power of an argument by 3
power3 = lambda number: number ** 3
print(f'Answer = {power3(2)}')

# using a lambda expression in a function 
def basicMath(number):
    return lambda num : num + number
result = basicMath(23)
print(result)
print('Result: %d'%result(13))

