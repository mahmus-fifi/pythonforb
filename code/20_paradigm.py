# OOP Paradigm 
"""
#Abstraction 
name = 'Peter'
num = 0
for characters in name:
    num+= 1
print('there are %d characters in the string: %s' %(num, name))

# using a built in function 
print(f'length of characters in {name} is: {len(name)}')

#2Inheritance 
class Parent():
    def __init__(self, name):
        self.name = name
    def PrintWord(self):
        print(self.name)
        
class Son(Parent): # inheriting the methods from the Parent() class 
    pass

#creating an instance 
vader = Parent('Darth Vader')
print(vader.name)

#creating an instance for the son
luke = Parent('Luke Skywalker')
print(luke.name)


"""
# using polymorphism 
class Laptops:
    def HasGpu(self):
        print('some laptops have a dedicated GPU')
        
class FriendsLaptop(Laptops):
    def HasGpu(self):
        print('no gpu present')
        
class TeacherLaptop(Laptops):
    def HasGpu(self):
        print('Has a gpu as well')
        
# create our instances 
obj_laptop = Laptops()
obj_teachers_laptop = TeacherLaptop()
obj_friend = FriendsLaptop()

obj_laptop.HasGpu()
obj_teachers_laptop.HasGpu()
obj_friend.HasGpu()
    
    
    
















