class Car:
    def move(self):
        print("The car is moving fast")

class Bike:
    def move(self):
        print("The bike is moving slowly")

def make_move(vehicle):
    vehicle.move()

car = Car()
bike = Bike()

make_move(car)
make_move(bike)