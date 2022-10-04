# working with list slicing 

items = ['apple','box','cat','ship','matches','person','chill','fun']

slice = items[0]
slice1 = items[2:4] # starts slicing from the second to third
slice2 = items[4:] # starts slicing from the fourth item to last 
slice3 = items[-1] # starts from the last item, returns 'fun'
slice4 = items[-3:-1] # reverse slices from third item to second, excluding the first 
slice5 = items[-4:-1] # empty list if we try -1 to -4
slice6 = items[:4] # begins slice from first  to fourth 

# different ways to display our output 
print(items)
print(f'{items[0]} is at index: {items.index("apple")}')
print(f'first slice: {slice}')
print('slice1 :' +str(slice1)) # concat to str or else error!
print(f'slice1: {slice1}') # using f-strings
print('slice2: %s' %slice2) # using format specifiers 
print('slice3: {}'.format(slice3)) # using format specifiers 2 
print('slice4: {}'.format(slice4))
print(f'Reverse slicing from -1 to -4 gives: {slice5}')
print('slice6: %r'%slice6)









