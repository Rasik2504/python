from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Bike(Vehicle):
    def start(self):
        print("Bike is started")
class Car(Vehicle):
    def start(self):
        print("Car is Started")
car=Car()
bike=Bike()
car.start()
bike.start()