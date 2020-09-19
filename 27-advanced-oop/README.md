# Advanced OOP principles

## SOLID design principles

<br>

### 1. Single-responsibility Principle
> A class should only have a single responsibility. 

It should have one and only one reason to change.

Violating SRP:
```py
class Car:

   def __init__(self, speed: float, odometer: int):
       self.speed = speed
       self.odometer = odometer

   def accelerate(self):    
       return self.speed * 1.1

   def save_current_odometer(self):
       pass
```

The class above has two responsibilities:
1. calculating the speed after acceleration
2. saving current odometer value to a database

If database or the method to store data changes, we need to update this class. A common practice to make this class comply with SRP is to use the *facade design pattern*.


Adhering to SRP:
```py
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
```

In the example above the ```Car``` object is a facade for the database management.

<br>

### 2. Open–closed principle
> Objects or entities should be open for extension, but closed for modification.

Meaning that a class should be easily extendable without modifying the class itself.

Violating SRP:
```py
class Ford:
   def __init__(self, model: str, speed: float):
       self.model = model
       self.speed = speed

   def accelerate(self):
       if self.model == 'ranger':
           return self.speed * 1.1
       elif self.model == 'focus':
           return self.speed * 1.4
```

For any new Ford model we need to change the code above. The solution is to create a super class and then extend it in derived classes:

Adhering to SRP:
```py
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
```

<br>

### 3. Liskov substitution principle
> Objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program

In other words: if ```S``` is a subtype of ```T```, then objects of type ```T``` may be replaced by objects of type ```S```, without breaking the program. No matter how ```T``` has changed.

Adhering to SRP:
```py
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
```

In the above example, the type ```Ranger``` is a subtype of ```Ford```. Therefore, the instance ```ford```, although being a ```Ranger``` can be used as a substitute for ```Ford```.

Liskov is fundamental to a good object-oriented software design because it emphasizes *polymorphism* which is one of its pillars. A correct hierarchical design leads to flexible and polymorphic objects.

<br>

### 4. Interface segregation principle[
> Many client-specific interfaces are better than one general-purpose interface.

A client should never be forced to implement an interface that it doesn't use or clients shouldn't be forced to depend on methods they do not use.

This principle deals with the disadvantages of implementing big interfaces and promotes the creation of smaller more specific interfaces.

Violating SRP:
```py
class Car:

    def __init__(self, model: str, speed: float):
       self.model = model
       self.speed = speed

    def accelerate(self):
        return self.speed * 1.1

    def tow(self, device):
        print ('Tow a {device}')

class Hatch(Car):

    def accelerate(self):
        pass

    def tow(self, device):
        pass
```

In the code above, the small car is forced to implement a towing action. But it's not suitable for it.

Adhering to SRP:
```py
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
```

We fixed it by creating another more specific interface. Objects can implement ```FourWD``` if they want to.

<br>

### 5. Dependency inversion principle
> Entities should depend upon abstractions, not concretions.

It states that the high level module must not depend on the low level module, but they *both* should depend on abstractions.<br>
Also, abstractions should not depend on details. Details should depend on abstractions.

Violating SRP:
```py
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
```

In our example from the *Single-responsibility principle*, The ```Car``` is dependent on the lower module ```CarDB```. This makes them *tightly coupled*.

We can fix this by creating a contract which both will implement.

Adhering to SRP:
```py
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
```

The ```CarDB``` is implementing the interface ```IRepository```. The ```Car``` does not know anything about ```CarDB```. It just receives an ```IRepository```. But the injected object is capable of performing what has come in the contract.

<br>
<br>

### References

* [SOLID](https://en.wikipedia.org/wiki/SOLID)
* [S.O.L.I.D: The First 5 Principles of Object Oriented Design](https://scotch.io/bar-talk/s-o-l-i-d-the-first-five-principles-of-object-oriented-design)
* [SOLID Principles with Python Examples](https://medium.com/@vubon.roy/solid-principles-with-python-examples-10e1f3d91259)
* [S.O.L.I.D Principles explained in Python with examples.](https://medium.com/@dorela/s-o-l-i-d-principles-explained-in-python-with-examples-3332520b90ff)

<!-- 
Generics
-->
 