# class Car:

#     def __init__(self, model: str, speed: float):
#        self.model = model
#        self.speed = speed

#     def accelerate(self):
#         return self.speed * 1.1

#     def tow(self, device):
#         print ('Tow a {device}')

# class Hatch(Car):

#     def accelerate(self):
#         pass

#     def tow(self, device):
#         pass

class Car:

    def __init__(self, model: str, speed: float):
       self.model = model
       self.speed = speed

    def accelerate(self):
        return self.speed * 1.1

class FourWD:

    def tow(self, device):
        print ('Tow a {device}')

class Hatch(Car):

    def accelerate(self):
        pass
