# creating classes with python 
number = 23
name = 'GabbyCat'
fuel_price = 23.05
items = [number, name, fuel_price]

print(f'{type(number)},{type(name)},{type(fuel_price)}')
#help(int) 
fuel = round(fuel_price)
print('original value: %r, rounded value :%r' %(fuel_price, fuel))
letters = len(name)
print(f'number of text in {name} = {letters}')

for objects in items:
    print(objects)
print(f'type of items: {type(items)}')

# what do they have in common
# methods or functions 
# properties 

# creating a class 
class Laptop:
    pass 
print('laptop is of type: %s'%type(Laptop))

class LaptopNamer:
    def LaptopName(laptopname):
        return laptopname
# creating instances of the LaptopNamer 
mylaptop = LaptopNamer.LaptopName('Lenovo')
yourlaptop = LaptopNamer.LaptopName('Acer')

print('laptop name is: %s' %mylaptop)
print('laptop name is: %s' %yourlaptop)

class BookAuthor:
    def AuthorName(name):
        return name
# creating an instance 
author1 = BookAuthor.AuthorName('Stephen King')
print(f'Author name is: {author1}')

class AreaOfSquare():
    """Calculates the area of a square"""
    def Area(length):
        return length * length
    
square1 =AreaOfSquare.Area(4)
print('The area of square1 is: %d square meters'%square1)







        



