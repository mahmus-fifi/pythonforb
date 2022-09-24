# Using lists 
items = ['apple', 'cat','ship','mathces','person','chill','fun']

slice1 = items[2:4]
slice2 = items[4:]
slice3 = items[-1]
slice4 = items[-3:-1]
slice5 = items[-1:-4]
slice6 = items[:4]

print('First Slice:' +str(slice1))
print('slice2: %s' %slice2)
print('slice3: {}'.format(slice3))
print(f'slice4 (reverse slices form the negative third to negative first item):{slice4}')
print(slice5)
print(f'slice6: {slice6}')
