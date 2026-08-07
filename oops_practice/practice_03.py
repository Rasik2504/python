class student:
    def __init__(self,name,age,mark):
        self.name=name
        self._age=age
        self.__mark=mark
    @property 
    def mark(self):
        return self.__mark
    @mark.setter
    def mark(self,new_mark):
        if new_mark>0:
            self.__mark=new_mark
        else:
            print("Invalid mark")
    

    def display(self):
        print("Name:",self.name)
        print("Age:",self._age)
        print("Mark:",self.__mark)

student1=student("Anisha",19,89)
student1.mark=60
print("Mark:",student1.mark)
