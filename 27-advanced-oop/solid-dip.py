class IRepository:

    def Add(self, entity):
        pass

class CarDB(IRepository):

   def Add(self, entity):
       pass

class Car:

   def __init__(self, repository: IRepository, odometer: int):
       self.odometer = odometer
       self._repo = repository

   def save_current_odometer(self):
       self._repo.add(obj=self)