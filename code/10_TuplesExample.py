# working with tuples 
numbers = (23,5,33,44,'hi')
print(type(numbers))

counting_items = numbers.count(23)
print(f'The number of times 23 occurs in the tuple {numbers} is: {counting_items}')

# accessing items in tuples 
print(numbers[4])
# negative indexing 
print(numbers[-2])

# ranged indexing 
print(numbers[1:3])

# checking items in a list 
if 'hi' in numbers:
    print("Yup, 'hi' is in the numbers tuple")
    
# getting the length of a tuple 
length_of_numbers = len(numbers)
print(f'There are {length_of_numbers} items in this tuple')

# strange case 
i_am_alone = ("Home Alone",)
print(type(i_am_alone))

# converted tuple to list
numbers_as_lists = list(numbers)
numbers_as_lists.append("Y2K")
print(numbers_as_lists)

# reconvert to a tuple
numbers = tuple(numbers_as_lists)
print(numbers)
print(type(numbers))








