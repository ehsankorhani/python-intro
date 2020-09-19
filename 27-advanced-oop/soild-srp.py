# class Car:

#    def __init__(self, speed: float, odometer: int):
#        self.speed = speed
#        self.odometer = odometer

#    def accelerate(self):    
#        return self.speed * 1.1

#    def save_current_odometer(self):
#        pass

class CarDB:

   def save_current_odometer(self, obj):
       pass

class Car:

   def __init__(self, speed: float, odometer: int):
       self.speed = speed
       self.odometer = odometer
       self._db = CarDB()

   def accelerate(self):    
       return self.speed * 1.1

   def save_current_odometer(self):
       self._db.save_current_odometer(obj=self)
