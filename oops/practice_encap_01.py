class Student:
    def __init__(self,name):
        self.__name=name
    def show_name(self):
        print(self.__name)
s1=Student("Alice")
s1.show_name()