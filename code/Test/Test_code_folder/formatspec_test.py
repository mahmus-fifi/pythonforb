from math import pi
name = "Musa"
surname = "Tukur"
middle_name = "Usman"
print(name)
print("user_name is: %s" %name) # single variable

print("Firstname:%s middle_name:%s Surname:%s" \
      % (name, middle_name, surname)) # more than one variable 

print(pi) # prints pi in all its glory 
# print pi to 2 significant figures 
print("Pi to two sf: %.2f" %pi)
# adding some padding to the output 
print("Pi to two sf: %20.2f" %pi)

# formatting output 
title = "Price Per Product:"
title2 = "Amount:"

print("%s %d" %(title, 234))
print("%10s %d" %(title2, 6))

# other format specifiers 
""" "%"d --- use with integers
    "%f" --- use with floating point numbers 
    "%s" --- use with strings 
    "%d%%" --- to add a percent sign %
"""
# adding spaces 
"""
    "%6d" -- adds 6 spaces 
    "%06d" -- adds 6 zeros after the number 6. 
    "%.2f" -- displays two digits after the decimal point 

"""