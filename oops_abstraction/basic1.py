from abc import ABC,abstractmethod
class Animal:
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Dog Barks")
class Cat(Animal):
    def sound(self):
        print("Cat Meows")
animal=[Dog(),Cat()]
for i in animal:
    i.sound()