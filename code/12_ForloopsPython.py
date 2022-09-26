# working with Python forloops
programming_languages = ['Python', 'C++', 'Java,','C','Swift','JavaScript']

"""
for languages in programming_languages:
    print(languages)
    
state = 'Mississippi'

for letters in state:
    print(letters)
    """
# breaking out of a for loop 

"""for lang in programming_languages:
    if lang == 'Swift':
        #break
        continue
    print(lang)"""
# using numerical values and range() 
"""number = 10
for val in range(number):
    print(f'Values are: {val}')    
"""
"""start = 2
stop = 21
step = 3

for i in range(start, stop, step):
    print(i)
    
for val in range(1, 10, 4):
    print(val)"""

"""   
for num in range(12):
    print(num)
else:
    print('Loop Executed Successfully')
    
for y in range(10):
    if y == 4:break
    print(y)
else:
    print("Loop finally Executed!")
# nested forloops    
widths = [23, 2, 45]
heights = [12, 3, 8]

for i in widths:
    for j in heights:
        print(i, j)

for i in widths:
    pass       
    
game = ['God of War', 'Gears of War', 'Zelda']
console = ['PS5', 'Xbox Series S', 'Nintendo']

for i in game:
    for j in console:
        print(i, j) 
 """       
########## Exercises 
for row in range(3):
    for column in range(3):
        print(row, column) 
    






    