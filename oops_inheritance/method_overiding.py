class Vehicle:
    def fuel(self):
        print("Vehicle Use Fuel")
class Car(Vehicle):
    def fuel(self):
        print("Car use petrol")
class ElectricCar(Vehicle):
    def fuel(self):
        print("Electiricy")
v1=Vehicle()
c1=Car()
e1=ElectricCar()
e1.fuel()