class Obj:
    pass

class Car:
    make = 'GMC'
    model = 'Suburban'

car1 = Car()
car2 = Car()

print(Car.__dict__)
print(car1.__dict__)
print(car2.__dict__)


print(Car.model) # Suburban
print(car1.model) # Suburban