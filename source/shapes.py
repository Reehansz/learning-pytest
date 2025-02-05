import math
class Shapes:
    def area(self):
        pass
    def perimeter(self):
        pass

class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return (math.pi * math.pow(self.radius, 2))
    
    def perimeter(self):
        return (2 * math.pi * self.radius)
    
class Rectangle(Shapes):

    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * self.length * self.width
    