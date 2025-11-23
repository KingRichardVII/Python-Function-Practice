#object = instance of a class

"""
class = blueprint
    describes the attributes and methods our object will have
    naming convention capitalized

we use programming to mimic real world objects: phone, TV, bag of chips
    assign attributes = is/has --- ex: name, age, height
    assign methods = actions, what the object can do -- ex: eat, sleep, code

You can also create a separate file for just the class if it is very large
    Then, in your main file, run:
    from [filename] import [Class name]

We have a special initializer method to pass ARGUMENTS and ASSIGN them to the object's attributes

Think of self as replacing the name of the object we created
    ex: self = car_1
"""

class Car:
#we require a special method called the initialize method to construct objects for us
#aka constructor
    def __init__(self, make, model, year, color):
    #what are a few attributes a car might have?
        self.make = make #self referring to the current object we're working on or creating
        self.model = model # = model, where it is whatever input we set for the parameter
        self.year = year
        self.color = color

#what kinds of methods(actions) does a car perform?
    #a car can drive
    def drive(self): # self refers to the OBJECT using this method
        print("This " + self.model + " is driving")
    #a car can stop
    def stop(self):
        print("This " + self.model + " is stopping")

#create an object called car_1 with the following attributes that are passed to the class
car_1 = Car("Chevy","Corvette",2021,"blue")

#access and print each attribute
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

#make the object use the drive method
car_1.drive() #we do not need to pass anything to self -> drive(self)
car_1.stop()

#we can use the same class to create MORE cars(objects)
car_2 = Car("Honda","Civic",2015,"Gray")

car_2.drive()
car_1.stop()
