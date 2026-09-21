class Car:
    def move(self):
        print("Car is moving")


class Bike:
    def move(self):
        print("Bike is moving")


vehicles = [Car(), Bike()]

for vehicle in vehicles:
    vehicle.move()