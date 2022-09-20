"""Working with list methods"""

# testing some list methods here
home = ["mahmud", 2, "mama", 6, "easy", 3, "grandma", 8 , 8 , 67, 8]
print(home.index("mama")) # print the index of the item in the method
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
"""our_list = []
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
"""
"""items = ['God of war', 'Resident Evil 3','zelda' ,'Tekken Tag Tournament','Ace Combat']
sorted_items = sorted(items)
print(f'Items in the list are: {sorted_items}')
items.pop(0)
print(items)
"""

# test sorting
numbers = [1,3,5,2,1,5,4,2,2,1,1,1,]
numbers.sort()
print(f'Listing the Items in the list:{numbers}')

"""
we haven't changed (mutated) any items in the list
if we do and try to print it, python will return NONE. none is a python object
that tells us that the object dosent have a datatype that represents it. when we mutate a list 
using list methods such as append() or sort(), Python knows that we have changed the list and to prevent 
errors it assigns a value  'None' to the new mutated list to prevent reference conflict from the original list.

name = 'string'
name = ''
name = None 

let's mutate the list and see what happens 

can we create an empty list and store the reference of the mutated list to prevent seeing None as our output? :smile: let's try 
"""



