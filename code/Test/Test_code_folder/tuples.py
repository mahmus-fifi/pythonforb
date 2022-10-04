# tuples are ordered and unchanged, we cant mutate them 
numbers = (23,5,33,44,'hi')
print(f'Data type is: {type(numbers)}')
print(f'items in numbers are: {numbers}')

counting_items = numbers.count(23)
print(counting_items)

# accessing tuples 
print(numbers[3]) # zero indexed 
print(numbers[-1]) # negative indexing tuples 

# range indexing 
print(numbers[2:5])

# checking items in tuples 
if 'hi' in numbers:
    print("yup, 'hi' is in the numbers tuple")

# getting the length 
length_of_numbers = len(numbers)
print(f'There are {length_of_numbers} items in this Tuple')

# strange case 
unity3d = ("Unity Game Engine",) # add comma tell python it is a tuple 
print(type(unity3d))


numbers_as_lists = list(numbers) # convert numbers to a list 
numbers_as_lists.append("Y2K")
print(numbers_as_lists)

numbers = tuple(numbers_as_lists)
print(numbers)
print(type(numbers))

# why tuples or lists 
# you cant mutate them, so this is good for a secure app 
# it could run efficiently 
# tuple, ordered and unchangable 
# list, ordered and changable  
