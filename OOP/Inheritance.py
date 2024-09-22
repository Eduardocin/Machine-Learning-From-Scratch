"""
    Inheritance : allows a class to inherit attributes and methods from anothes class 
    helps with code resuability and extensibility
    Syntax :
        class Child(Parent):
"""

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
        
    def eat(self):
        print(f"{self.name} is eating.")
        
    def sleep(self):
        print(f"{self.name} is sleeping.")
        
        
class Dog(Animal):
    pass

class Cat(Animal):
    pass

mimo = Cat("Mimo")
print(mimo.name)

# Import the ABC (Abstract Base Class) and abstractmethod from the abc module  
from abc import ABC, abstractmethod  

# Define a base class called Shape that inherits from ABC  
class Shape(ABC):  
    # Define an abstract method called area that must be implemented by any subclass  
    @abstractmethod  
    def area(self):  
        # This method is abstract, so it doesn't have an implementation  
        pass  # The pass statement is used to indicate that this method is abstract  

    # Define another abstract method called perimeter  
    @abstractmethod  
    def perimeter(self):  
        # This method is also abstract, so it doesn't have an implementation  
        pass  # The pass statement is used to indicate that this method is abstract  

# Define a subclass called Circle that inherits from Shape  
class Circle(Shape):  
    # Define an initializer method to set the radius of the circle  
    def __init__(self, radius):  
        # Set the radius attribute of the circle  
        self.radius = radius  

    # Implement the area method that was defined as abstract in the Shape class  
    def area(self):  
        # Calculate the area of the circle using the formula πr^2  
        return 3.14 * self.radius ** 2  

    # Implement the perimeter method that was defined as abstract in the Shape class  
    def perimeter(self):  
        # Calculate the perimeter of the circle using the formula 2πr  
        return 2 * 3.14 * self.radius  

# Define another subclass called Rectangle that also inherits from Shape  
class Rectangle(Shape):  
    # Define an initializer method to set the width and height of the rectangle  
    def __init__(self, width, height):  
        # Set the width and height attributes of the rectangle  
        self.width = width  
        self.height = height  

    # Implement the area method that was defined as abstract in the Shape class  
    def area(self):  
        # Calculate the area of the rectangle using the formula width * height  
        return self.width * self.height  

    # Implement the perimeter method that was defined as abstract in the Shape class  
    def perimeter(self):  
        # Calculate the perimeter of the rectangle using the formula 2 * (width + height)  
        return 2 * (self.width + self.height)  

# Try to instantiate the Shape class directly (this will raise an error)  
try:  
    shape = Shape()  
except TypeError as e:  
    # Print the error message  
    print(e)  

# Instantiate the Circle and Rectangle classes  
circle = Circle(5)  
print(circle.area())  # Print the area of the circle  
print(circle.perimeter())  # Print the perimeter of the circle  

rectangle = Rectangle(4, 5)  
print(rectangle.area())  # Print the area of the rectangle  
print(rectangle.perimeter())  # Print the perimeter of the rectangle