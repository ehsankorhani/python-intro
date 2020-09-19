# class Ford:

#    def __init__(self, model: str, speed: float):
#        self.model = model
#        self.speed = speed

#    def accelerate(self):
#        if self.model == 'ranger':
#            return self.speed * 1.1
#        elif self.model == 'focus':
#            return self.speed * 1.4

class Ford:

   def __init__(self, model: str, speed: float):
       self.model = model
       self.speed = speed

   def accelerate(self):
        return self.speed * 1.1

class Ranger(Ford):

   def accelerate(self):
       return super().accelerate()

class Focus(Ford):

   def accelerate(self):
        return super().accelerate() * 1.3