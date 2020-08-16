class Car:
    models = []
    count = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        Car.count += 1

    @classmethod
    def add_models(cls, make):
        cls.models.append(make)

    @staticmethod
    def convert_km_to_mile(value):
        return value / 1.609344


class Pickup(Car):
    pass

car1 = Car('Ford', 'Ranger')
car2 = Car('Nissan', 'Skyline')

car1.add_models('BMW')

print(Car.models)
print(car2.models)

print(Car.count)

print (Car.convert_km_to_mile(10))
print (car1.convert_km_to_mile(10))