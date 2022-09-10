# lessons on format specifiers 
from math import pi
name = "Musa"
middle_name = "Tukur"
surname = "Usman"
print(name)

print("%s" %name)
# using format specifier 
print("firstname:%s middlename:%s surname:%s" %(name, middle_name, surname))

print(pi)
# print pi to 2 significant figures 
print("pi to two significant figures is: %.3f" %pi)

# example 2 
title = "price per product:"
title2 = "amount:"
num = 125
num2 = 12
print("%s %d" %(title, num))
print("%18s %d" %(title2, num2))

# other format specifiers 
"""
"%s" -- used with strings 
"%d" -- used with integers 
"%r" -- generally used for strings or integers 
"%d%%" -- used to add a percent 

"%10d" -- used to add padding, this will add 10 spaces 
"%05d" -- add 5 zeros 
"%.2f" -- show only 2 digits after the decimal point 
"""
num2 = 23
print("%d%%" %num2)
