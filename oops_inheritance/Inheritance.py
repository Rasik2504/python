class Animal:
    def eat(self):
        print("Animal Eat")
    def sleep(self):
        print("Animal Sleep")
class Dog(Animal):
    def bark(self):
        print("Dog Barks")
e1=Dog()
e1.eat()
e1.bark()