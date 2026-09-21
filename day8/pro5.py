import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_circumference(self):
        return 2 * math.pi * self.radius

circle = Circle(7)

print("Circumference of Circle:", circle.calculate_circumference())