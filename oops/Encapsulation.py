class car:
    def __init__(self,carname,no_wheel):
        self.carname=carname
        self.__no_wheel=no_wheel
    def __del__(self):
        print(self)
    def __str__(self):
        return self.carname

    def get_data(self):
        return self.__no_wheel
    def set_data(self,no_wheel):
        self.__no_wheel=no_wheel

    def move_frwd(self):
        return self.carname
    

s1=car("swift",4)
s1.set_data(9)
print(s1.get_data())