# creating classes with python 
number = 23
name = 'GabbyCat'
fuel_price = 23.05
items = [number, name, fuel_price]
print(f'{number} is of type: {type(number)},{name} is of type: {type(name)},{fuel_price} is of type: {type(fuel_price)}')
#help(str)

fuel = round(fuel_price)
print(fuel)

letters = len(name)
print('number of character in name: %s' %letters)
print(len(name))

# creating an empty class 
class Laptop:
    pass
    
#print('laptop is of type: %s'%type(Laptop))

class LaptopNamer(object):
    def LaptopName(laptopname):
        return laptopname
# create object of the class aka instances 
mylaptop = LaptopNamer.LaptopName('Lenovo')
print('laptop name is: %s' %mylaptop)

yourlaptop = LaptopNamer.LaptopName('Acer')
print(f'your laptop name is: {yourlaptop}')

class BookAuthor():
    def AuthorName(name: str):
        return name
author1 = BookAuthor.AuthorName('Stephen King')
print('name of author: %s' %author1)

class AreaOfSquare():
    """Calculates the Area of a Square"""
    def Area(length: float):
        return length * length
    
# instance of the class 
square1 = AreaOfSquare.Area(4.23)
print(square1)
print('The Area of square1 is: %r square meters' %square1)
print(f'The Area of square1 is :{square1:.2f} square meters')

square2 = AreaOfSquare.Area(12.55)
print(f'The Area of square2 is :{square2:.2f} square meters')




