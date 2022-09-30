# Using Dictionaries 
game_console_ps = {
    'Company:':'Sony',
    'Console:':'PS',
    'ReleaseYear(Japan):': 'December 3 1994',
    'ReleaseYear(North America):': 'September 9 1995',
    'Cost(JPY):': 39800,
    'Cost(USD):': 299,
    'Cost(GBP):': 299  
   }
"""w
print(type(game_console_ps))
# print the output 
print(game_console_ps)
# stuff about dictionaries 

Dictionary items are ordered, mutable(can change), are created using key:value pairs 
referenced using key names []
can't have items with the same key 
eg 
course = {
    'math101': 56
    'math103': 24
    'date': 1996
    'date': 1996    
}

# print Japanease release year value
 
cost_in_yen = game_console_ps['Cost(JPY)']
print(f'In 1994 the original Play Stations costs {cost_in_yen} Yen. It was quite pricy.')

# use get() method to get the values in a dictionary 

company_name = game_console_ps.get('Company')
print(f'{company_name} has always been a leader in the gaming console market.')


# length of a dictionary using len() method 
print(f"With a dictionary of {len(game_console_ps)} items, i dare say it's rather short.")

# use key() to get all keys in the dictionary, this is called the dictionary view  
console_keys = game_console_ps.keys()
print(console_keys)

# adding items to our dictionary 
game_console_ps['UnitsShipped'] = '102.49 Million'
print(f'our new dictionary: {game_console_ps}')

# get all values in the dictionary using values()
all_values = game_console_ps.values()
print(all_values)

# items() will return values in the dictionary as tuples 
tup = game_console_ps.items()
print(tup)
"""
# using statements to check for key values 
#if 'Console' in game_console_ps:
    #print('Console exists as a dictionary key')

# changing dictionary items using key names 
game_console_ps['ReleaseYear(North America)'] = 1996 # changing the release year from 'September 9 1995' to 1996
#print(game_console_ps)

# let's use the update method to update the dictionary 
game_console_ps.update({'Cost(USD)': 300})
#print(game_console_ps)

# to remove items in a dictionary, use the pop() method 
# popitem() removes last item in dict
# del dict["key"]
# del (dictionary)
#game_console_ps.pop('Cost(GBP)')
#print(game_console_ps)

# clear() Empties the dictionary 

ages_dict = {'Amber':21,
             'Peter': 29,
             'Sherrif': 25,
             'Mode': 18}
print(ages_dict) # defore removing last item 
ages_dict.pop('Sherrif')
#print(f'{ages_dict}: Bye Sherrif!')

"""For looping through a dictionary"""
# print key names
for things in ages_dict:
    print(f'we have: {things} in the dictionary')
    
# print value names using forloop 
for vals in ages_dict:
    print(ages_dict[vals])

# printing all values using values()
for v in ages_dict.values():
    print(v)

# looping through keys in the dict 
for superkeys in ages_dict.keys():
    print(superkeys)
    
# print both key and values 
for k,v in ages_dict.items():
    print(k,v)
    
for k,v in game_console_ps.items():
    print(k,v)
   
# Copying a Dictionary using copy() and dict()

new_console_dict = game_console_ps.copy()
print(new_console_dict)

# or you can use 
console_info = dict(game_console_ps)
print(f'New Console Info: {console_info}')

"""Nested Dictionaries"""
# style A 
# Dict:  {"DictA":   {"KeyA":"ValueA"},
#         "DictB":   {"KeyB":"ValueB"},
#         "DictC":   {"KeyC":"ValueC"}

# Style B
"""
DictA = {
    "KeyA": "ValueA",
    "KeyB: "ValueB",
    "KeyC: "ValueC"
}
DictB = {
    "KeyA": "ValueA",
    "KeyB: "ValueB",
    "KeyC: "ValueC"   
}
DictC = {
    "KeyA": "ValueA",
    "KeyB: "ValueB",
    "KeyC: "ValueC"
}
AllThreeDictionaries = {
    "DictA": DictA,
    "DictB": DictB,
    "DictC": DictC
}
"""
my_gaming_consoles = {
    'FirstConsole': {'name': 'Xbox',
                    'Year': 2012,
                    'Favourite Game': 'Ray man'},
    
    'SecondConsole': {'name': 'PS',
                      'Year': 1998,
                      'Favourite Game': 'GrandTourismo'},
    
    'ThirdConsole': {'name': 'PS 2',
                     'Year':2004,
                     'Favourite Game': 'Mortal Kombat'}
                    }
carrot_cake = {
    "name":"CarrotCake",
    "cost":3000,
    "calories": 0.34
}
cup_cake = {
    "name":"CupCake",
    "cost":5000,
    "calories":0.54
}
sponge_cake = {
    "name":"SpongeCake",
    "cost":8000,
    "calories":2000
}
fifis_cake_gallery = {
    "CarrotCake":carrot_cake,
    "CupCake":cup_cake,
    "SpongeCake":sponge_cake
}




























