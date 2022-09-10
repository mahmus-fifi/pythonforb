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
