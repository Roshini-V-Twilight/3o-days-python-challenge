class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

rectangle = Rectangle(10, 5)

print("Area of Rectangle:", rectangle.calculate_area())