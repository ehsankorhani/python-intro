import abc

class CarFactory():
    def create_car(self, type, engine):
        if type == 'Sedan':
            return Sedan(engine)

        elif type == 'Pickup':
            return Pickup(engine)

        elif type == 'SUV':
            return SUV(engine)

        elif type == 'Coupe':
            return Coupe(engine)

        raise Exception('Error! Unknown vehicle.')

class Car(metaclass=abc.ABCMeta):
    def start(self):
        print (f'The {self.engine} engine is starting...')


class Sedan(Car):
    def __init__(self, engine):
        self.doors = 4
        self.engine = engine

class Pickup(Car):
    def __init__(self, engine):
        self.doors = 2
        self.engine = engine

class SUV(Car):
    def __init__(self, engine):
        self.doors = 5
        self.engine = engine

class Coupe(Car):
    def __init__(self, engine):
        self.doors = 2
        self.engine = engine


car_factory = CarFactory()

my_x5 = car_factory.create_car("SUV", "v8")
my_miata = car_factory.create_car("Coupe", "v4")

my_x5.start()
my_miata.start()
