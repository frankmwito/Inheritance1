# Shape Area inheritance

import math

# Base Shape class
class Shape:
    def __init__(self, color):
        self.color = color
    
    def area(self):
        pass

# Circle subclass
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
        
    def area(self):
        return math.pi * math.pow(self.radius, 2)

# Rectangle subclass
class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Creating instances of Circle and Rectangle
circle1 = Circle("brown", 5)
print(f"Area of the circle is: {circle1.area()}")

rectangle1 = Rectangle("orange", 3, 9)
print(f"Area of the rectangle is: {rectangle1.area()}")
