#single Inheritance
class vehicle:
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
class car(vehicle):
    def __init__(self,carname,no_wheel,air_bag):
        super().__init__(carname,no_wheel)
        self.air_bag=air_bag

s2=car("Swift", 4, 7)
print(s2.carname)

    