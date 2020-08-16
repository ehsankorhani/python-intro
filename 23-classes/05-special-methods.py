class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_description(self):
        return '{0} {1}'.format(self.make, self.model)

    def __repr__(self):
        return "Car('{}', '{}')".format(self.make, self.model)

    def __str__(self):
        return "{} - {}".format(self.make, self.model)

my_car = Car('Ford', 'Ranger')

print(my_car.__repr__())
print(my_car.__str__())