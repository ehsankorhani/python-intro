from datetime import datetime

class Car:
    _odometer = None
    __registration_plate = None

    def get_odometer(self):
        return f'{self._odometer:,} km'

    def set_odometer(self, value):
        self._odometer = value


car1 = Car()

print(car1._odometer)
# print(car1.__registration_plate)
print(car1._Car__registration_plate)

car1.set_odometer(25800)
print(car1.get_odometer())

# ----------------------------------------------------------

class Vehicle:

    @property
    def rego_expiry(self):
        return f'{self.__rego_expiry} GMT'
    
    @rego_expiry.setter
    def rego_expiry(self, value):
        today = datetime.today().strftime('%Y-%m-%d')
        if (value < today):
            value = 'Expired'
        self.__rego_expiry = value
 
    @rego_expiry.deleter
    def rego_expiry(self):
        del self.__rego_expiry


my_vehicle = Vehicle()

my_vehicle.rego_expiry = '2020-09-15'
print(my_vehicle.rego_expiry)

del my_vehicle.rego_expiry
# print(my_vehicle.rego_expiry) # 'Vehicle' object has no attribute '_Vehicle__rego_expiry'

# -------------------------------------------------------

class Auto:
    odometer = None

    def __init__(self):
        self.odometer = 0

car2 = Auto()

car2.odometer = 25800
print(car2.odometer) # 25000