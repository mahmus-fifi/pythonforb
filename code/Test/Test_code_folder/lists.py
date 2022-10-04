"""Working with list methods"""
"""
# testing some list methods here
home = ["mum", 2, "dad", 6, "baby", 3, "grandma", 8 , 8 , 67, 8]
print(home.index("grandma")) # print the index of the item in the method
print('the third item in home is: %r' %home[2])
print(f'The number 8 occurs: {home.count(8)} times')

# string to experiment with: place
place = "poolhouse"

# Use upper() on place: place_up
place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place
print(place.count("o"))

# working with lists 
our_list = []
# adding data to a list 
our_list.append("ps5")
our_list.append("xbox1 s")
our_list.append(230.34)
# muting objects in a list 
our_list[0] = 'ps4'
# setting a float value for the second index in our_list 
our_list[1] = 500.67
# removing elements in a list using del 
#del our_list[0]
print('items in the list :%r' %our_list)

items = ['God of war', 'Resident Evil 3','zelda' ,'Tekken Tag Tournament','Ace Combat']
sorted_items = sorted(items)
print(f'Items in the list are: {sorted_items}')
items.pop(0)
print(items)

# test sorting
# numbers = [1,3,5,2,1,5,4,2,2,1,1,1,]
# numbers.sort()
# print(f'Listing the Items in the list:{numbers}')

"""

"""we haven't changed (mutated) any items in the list
if we do and try to print it, python will return NONE. none is a python object
that tells us that the object dosent have a datatype that represents it. when we mutate a list 
using list methods such as append() or sort(), Python knows that we have changed the list and to prevent 
errors it assigns a value  'None' to the new mutated list to prevent reference conflict from the original list.
"""
# using sort 
letters = ['a','b','b','g','a','a']
letters.sort()
print(letters.sort()) # returns none because the print method is 
# not returning the result of the 'letters.sort()'
# this will work if we use a function to return the value of the sorting
print(letters)
r = print(letters.sort())
print(type(r)) # r is a NoneType object 


# using sorted
new_letters = []
print(type(new_letters))
new_letters = print(sorted(letters))

"""
append()	   Adds an element at the end of the list
clear()	       Removes all the elements from the list
copy()	       Returns a copy of the list
count()	       Returns the number of elements with the specified value
extend()	   Add the elements of a list (or any iterable), to the end of the current list
index()	       Returns the index of the first element with the specified value
insert()	   Adds an element at the specified position
pop()	       Removes the element at the specified position
remove()	   Removes the first item with the specified value
reverse()	   Reverses the order of the list
sort()	       Sorts the list
"""
# sort is a method of the list class and can only be used with lists 










