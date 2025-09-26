# O.O Notes with explanations etc:
# class is like a blueprint for creating objects
# an object is an actual thing created using a class
# instantiating a class is creating an object using the classes ' blueprint ' 
# self refers to the current object of a class. When you create an object, self lets you store and/or access data inside that specific object.
# - you must include self as the first parameter of every method inside a class, so python knows you're refering to the current object. 
#
#
#
#
#
#
#
#


'''
define a class called vegetable with following attributes and methods
* name
* colour
* weight

% set_colour
% get_colour
% set_weight
% get_weight

'''

# class definition
class vegetable:

    # Constructor, sir said something about exam papers calling it ' new ' instead. 
    def __init__(self, name, colour, weight):
        
        self.name = name
        self.colour = colour
        self.weight = weight

# main

    def set_veg_colour(self, colour):
        self.colour = "Orange"
    
    def set_veg_weight(self, weight):
        self.weight = 10
    
    def get_weight(self):
        return self.weight
    
    def set_colour(self, new_colour):
        self.colour = new_colour

    def get_colour(self):
        return self.colour
    
# end class

# instantiate the class, call it my_veg and give it a name
# This is also called an object(instance of a class)
my_veg = vegetable("Carott", "Orange", 10)
print(my_veg.name)

# set colour and weight


# use a getter to get the weight 
weight = my_veg.get_weight()
print(weight)

# change the colour
my_veg.set_colour("Blue")
colour = my_veg.get_colour()
print(colour)


class human: 

# Need to master this ^^^^ and also inheritance, how to call the parent constructor, and creating an inheritance class - going to be on the mock

