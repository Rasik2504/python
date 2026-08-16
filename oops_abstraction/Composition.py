class Battery:
    def charge(self):
        print("Battery is charging")
class Laptop:
    def __init__(self,battery):
        self.battery=battery
    def use_laptop(self):
        self.battery.charge()
        print("Laptop is Running")
battery=Battery()
laptop=Laptop(battery)
laptop.use_laptop()