# using format specifiers part 2 
# f - strings  
"""name = input("Enter your name: ")
print("you entered: " +name)

greeting = "Please enter your age:"
age = input(greeting)
print("you are: " +age + " years old")

# f- string example 
print(f"Hi there {name} wow so you are {age} years old. cool")
"""
# f-string example 2 
"""
num = 23.45 
num2 = 0.0345
solution = num * num2 

print(f"the result of mulitplying {num} by {num2} is {solution}")

print(f"the result of mulitplying {num} by {num2} is {solution: .2f}") # to two sf 
"""

# using f-strings with monetary values 
import fractions


expenses = 23454534
print(f"The total amount spent is: ${expenses:,}")

# example 3 
account_balance = 5000
groceries = 230.24

account_balance = account_balance - groceries
print(account_balance)
print(f"I spent N{groceries} on groceries, i have {account_balance:,.1f} left. Am broke")

fraction = .24 
print(f'According to the paper {fraction:.2%} of the students have laptops')

# lets print with f-strings v2 
print("my account balance, which is ${} is too low to buy an xbox1s".format(account_balance))

item = "milk"
item2 = "sugar"
item3 = "coffee"

print("Today, i bought a tin of {}, a box of {} and some sweet {} beans at the store."\
      .format(item, item2, item3))