class Ford:

   def __init__(self, model: str, speed: float):
       self.model = model
       self.speed = speed

   def accelerate(self):
        return self.speed * 1.1

class Ranger(Ford):
    
    def __init__(self, speed):
        super().__init__('Ranger', speed)

class Focus(Ford):

   def accelerate(self):
        return super().accelerate() * 1.3


ford = Ranger(100)
print (ford.accelerate())
