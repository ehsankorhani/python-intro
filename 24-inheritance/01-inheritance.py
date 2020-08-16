from abc import ABC, abstractmethod

class Boat(ABC):
    def __init__(self, id):
        self.id = id

    @abstractmethod
    def calculate_speed(self, value):
        pass

class FishingBoat(Boat):

    def __init__(self, id):
        super().__init__(id)

    def calculate_speed(self, value):
        return value + ' ml'


class Car:
    drivers = []
        
    def __init__(self, make, model):
        self.make = make
        self.model = model
            
    def get_description(self):
        return '{0} {1}'.format(self.make, self.model)

    def add_driver(self, name):       
        self.drivers.append(name)


class Pickup(Car):
    default_nickname = 'Driver'

    def __init__(self, make, model, payload):
        super().__init__(make, model)
        self.payload = payload

    def add_driver(self, name, nickname = None):
        if (nickname == None):
            nickname = self.default_nickname
        
        self.drivers.append(f'{name} {nickname}')
    

class FloatingHoverCar(Boat, Car):

    def __init__(self, id, make, model):
        Car.__init__(self, make, model)
        super().__init__(id)
    
    def calculate_speed(self, value):
        pass


my_pickup = Pickup('Ford', 'Ranger', 1132)
print (my_pickup.__dict__)
print (my_pickup.get_description())

#help(my_pickup)

my_pickup.add_driver('Jane')
my_pickup.add_driver('John', 'Mad Max')
print (my_pickup.drivers)

my_fishing_boat = FishingBoat('XYZ551')

#help(FloatingHoverCar)

my_hover = FloatingHoverCar('XYZ554', 'Renault', 'Float')
print (my_hover.get_description())

