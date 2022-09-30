game_console_ps = {
    'Company':'Sony',
    'Console':'PS',
    'ReleaseYear(Japan):':'December 3 1994',
    'ReleaseYear(NorthAmerica)':'September 9 1995',
    'Cost(JPY)': 39800,
    'Cost(USD)':299,
    'Cost(GBP)': 299
}
"""
#print(type(game_console_ps))
print(game_console_ps)

# print Japanease Release Year 
cost_in_yen = game_console_ps['Cost(JPY)']
print(f'In 1994 the original Playstation costs {cost_in_yen} Yen. Oops, it was quite pricey')

# getting the length of a dictionary 
print(f"With a dictionary of {len(game_console_ps)} items, i dare say it's rather short")


# getting the keys in a dictionary 
console_keys = game_console_ps.keys()
print(console_keys)

# adding items to the dictionary 
game_console_ps['UnitsShipped'] = '102.49 Million'
print(f'Our new dictionary with units shipped: {game_console_ps}')

# getting values from a dictionary 
all_values = game_console_ps.values()
print(all_values)

# using items() to return dictionary as tuple 
tup = game_console_ps.items()
print(tup)

# checking for an item in a dictionary 
if 'Console' in game_console_ps:
    print('Yes, Console Exists')
    
# changing dictionary items using key names 
game_console_ps['ReleaseYear(NorthAmerica)'] = 1996
print(game_console_ps)

# using the update() 
game_console_ps.update({'Cost(USD': 300})
print(game_console_ps)

# remove items in a dict pop()
# popitem() remove last item in dict 
# del dict["key"]
# clear()
"""


game_console_ps.pop('Cost(GBP)')
print(game_console_ps)

ages_dict = {
    'Amber': 21,
    'Peter': 29,
    'Nancy': 25,
    'Aisha': 18
}

print(ages_dict) # before clearing 
#ages_dict.clear() 
print(ages_dict) # after clearing 

"""Forlooping dictionaries"""
for things in ages_dict:
    print(f'we have {things} in the dictionary')
    
# print valuse in dict using for loop 
for vals in ages_dict:
    print(f'The ages in the dictionary are: {ages_dict[vals]}')

for key_dict in ages_dict.keys():
    print(key_dict)
    
# printing key and value pairs 
for k, v in ages_dict.items():
    print(k, v)
    
"""Copying dictionaries"""
# copy() method used to copy a dictionary 
new_console_dict = game_console_ps.copy()
print(new_console_dict)

# second method to copy dictionaries 
console_info = dict(game_console_ps)
print(f'New console info: {console_info}')


"""Nesting Dictionaries
# Style A
Dict: {"DictA":"ValueA"},
"DictB": {"KeyB":"ValueB"},
"DictC": {"KeyC":"ValueC"}

# Style B
DictA = {
    "KeyA":"ValueA",
    "KeyB":"ValueB",
    "KeyC":"ValueC"
}

DictB = {
    "KeyA":"ValueA",
    "KeyB":"ValueB",
    "KeyC":"ValueC"
}

DictC = {
    "KeyA":"ValueA",
    "KeyB":"ValueB",
    "KeyC":"ValueC"
}

AllThreeDictionaries = {
    "DictA":DictA,
    "DictB":DictB,
    "DictC":DictC
    
}


"""
# Example 
my_gaming_consoles = {
    'FirstConsole':{'name':'Xbox1',
                    'Year':2012,
                    'FavouriteGame':'Rayman Legends'},
    'SecondConsole':{'name':'PS',
                    'Year':1998,
                    'FavouriteGame':'GrandTourismo'},
    'ThirdConsole':{'name':'PS2',
                    'Year':2004,
                    'FavouriteGame':'Mortal Kombat'},
}
# Last Example 
    
carrot_cake = {'name':'CarrotCake',
        'cost':3000,
        'calories':0.34 }

cup_cake = {'name':'CupCake',
        'cost':5000,
        'calories': 0.54 }

sponge_cake = {'name':'SpongeCake',
        'cost':8000,
        'calories':200}

fifis_cake_gallery = {
    "CarrotCake":carrot_cake,
    "CupCake":cup_cake,
    "SpongeCake":sponge_cake
}

print(fifis_cake_gallery)
for k,v in fifis_cake_gallery.items():
    print(k,v)
    
    
    
    
    
    
    
    
    
















    











