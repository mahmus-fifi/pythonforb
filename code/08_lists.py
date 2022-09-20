# creating a list 
home = ['mum', 2, 'dad', 6.0, 'baby', 3, 'grandma',3,3,3,3,3,3,3,3,3,3,3,3]
#print(type(home))
print(home.index('baby')) # get the index position of objects in a list 
print('the third item in the list is: %r' %home[2])
print(f'The number of times 3 occurs in the list is: {home.count(3)}')

#print(help(list))

our_games = [] # empty list 
our_games.append("PS5")
our_games.append("Xbox1 s")
our_games.append("Nintendo Switch")
our_games[2] = 'Snes'
print(our_games)


names = ["Book", "Resident Evil 4", "Super Mario Galaxy","Ace Combat"]
print(names.sort())
print(names)

numbers = [12.33, 0.12, 34.33, 0.00001, 8]
numbers.pop(1)
numbers.sort(reverse= True)
print(numbers)
check = numbers.sort()
print(type(check))

sorted_numbers = sorted(numbers)
print(sorted_numbers)




