# working with variables and datatypes 
# integer, float, bool, string, char  
# set, dictionaries, lists, complex numbers 
# the equals sign = is the assignment operator 

# an integer or int is a positive or negative whole number 
# 12 , 24, -3 
account_balance = -3000 # created an integer variable 

# strings are a group of characters is a string and a char is a single character 
# we can use single '' or double quotes "" for strings 
name = "Mahmud" # string example 
single_letter = 'L' # example of a char 
surname = 'Shuaib'

#example adding variables 
age = 25
in_five_years = 5 

total = age + in_five_years
print(total)

# example of a float ie variable with a decimal point  
millimeter_value = 0.00234

# booleans are true or false values 
isEating = True
isSleeping = False 

# checking datatypes, tells us the datatype we are working with 
print(type(total))

#casting example 
num = 23.984
num2 = 20
solution = num * num2 
print(solution)
print(int(solution))