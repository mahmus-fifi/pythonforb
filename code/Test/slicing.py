# working with list slicing 

items = ['apple','box','cat','ship','matches','person','chill','fun']
slice1 = items[2:4] # starts slicing from the second to third
slice2 = items[4:] # starts slicing from the fourth item to last 
slice3 = items[-1] # starts from the last item, returns 'fun'
# different ways to display our output 

print('First Slice:' +str(slice1)) # concat to str or else error!
print(f'slice1:{slice1}') # using f-strings
print('Slice 2: %s' %slice2) # using format specifiers 
print('slice3: {}'.format(slice3)) # using format specifiers 2 





