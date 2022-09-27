# using dictionaries 
game_console_ps = {
    'Company':'Sony',
    'Console':'PS',
    'ReleaseYear(Japan)': 'December 3 1994',
    'ReleaseYear(North America)': 'September 9 1995',
    'Cost(JPY)': 39800,
    'Cost(USD)': 299,
    'Cost(GBP)': 299  
   }
print(type(game_console_ps))
# print the output 
print(game_console_ps)
# stuff about dictionaries 
"""
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
"""
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

# using statements to check for key values 
if 'Console' in game_console_ps:
    print('Console exists as a dictionary key')
    



















