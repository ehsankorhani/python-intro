class Car:
    # make = 'GMC'
    # model = 'Suburban'

    def __init__(self, make, model):
        # pass
        self.make = make
        self.model = model

    def get_description(self):
        # return '{0} {1}'.format(Car.make, Car.model)
        return '{0} {1}'.format(self.make, self.model)


car1 = Car('Ford', 'Ranger')
car2 = Car('Nissan', 'Skyline')

print(car1.get_description())
print(car2.get_description())