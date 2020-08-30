class Engine:

    def __init__(self, capacity, cylinder):
        self.capacity = capacity
        self.cylinder = cylinder

    def start(self):
        print(f'{self.cylinder} cylinder engine started!')

class Car():
    
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.engine = None


monsterEngine = Engine(6300, 12)
ecoEngine = Engine(1200, 4)

myFerrari = Car('Ferrari', 'GTC4')
myFerrari.engine = monsterEngine

myFerrari.engine.start()

