"""
while loop syntax 
while keyword 
condition :
indent the next block of code 
"""
"""number = 0 
while number < 4:
    print("Hello there")"""
    
"""
name = "" # empty string variable 
while name != "your name": # != not operator 
    print("kindly enter your name")
    name = input()
print("thanks for entering your name")
"""

# using the break statement 

"""while True:
    print("please enter username: ")
    user_name = input()
    if user_name == 'mahmus':
        break
    print("thanks for entering your name")
    """
"""number = 6
value = 0
while value < number:
    value = value + 1 # value += 1 
    if value == 4:
        continue
    print("numbers are: %d" %value)
"""
while True:
    user_name = input("please enter your name? ") 
    if user_name != "mahmus":
        continue
    correct_password = input(f"hello {user_name} enter the correct password: hint(your name)")
    if correct_password == user_name:
        break
    print(f"hello {user_name}")

# you can break out of an infinite loop using Ctrl + B key 
    
   
   
   
   
   
   
   
   
   
    
