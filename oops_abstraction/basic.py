from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car Starts with Key")
class ElectricCar(Vehicle):
    def start(self):
        print("Car start with touch")
Vehicles=[Car(),ElectricCar()]
for i in Vehicles:
    i.start()