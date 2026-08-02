class car:
    def __init__(self,carname,no_wheel):
        self.carname=carname
        self.no_wheel=no_wheel
    def __del__(self):
        print(self)
    def __str__(self):
        return self.carname

    def move_frwd(self):
        return self.carname
s1=car("Maruti",4)
print(s1.carname)
print(s1.no_wheel)
print(s1.move_frwd())