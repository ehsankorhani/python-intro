
# Inheritance

Inheritance models what is called an **is a** relationship. 

Inheritance definition in Python is also a bit different from the other C-type OOP languages. Rather then extending a Base class, the derived class will receive the Base as a parameter of the class definition.

```py
class Car:
    
    def __init__(self, make, model):
        self.make = make
        self.model = model
            
    def get_description(self):
        return '{0} {1}'.format(self.make, self.model)

class Pickup(Car):
    pass
```

At this point *Pickup* has access to all the methods and attributes of *Car*.

```py
my_pickup = Pickup('Ford', 'Ranger')

print (my_pickup.__dict__) # {'make': 'Ford', 'model': 'Ranger'}
print (my_pickup.get_description()) # Form Ranger
```

The ```help()``` function can reveal the *Method resolution order* of an instance of *Pickup* class.

```py
help(my_pickup)
```
```bash
 |  Method resolution order:
 |      Pickup
 |      Car
 |      builtins.object
```

<br>

### Constructor and ```super()```

Derived class can call base class constructor using ```super()```:

```py
class Car:
    
    def __init__(self, make, model):
        self.make = make
        self.model = model
            
    def get_description(self):
        return '{0} {1}'.format(self.make, self.model)


class Pickup(Car):

    def __init__(self, make, model, payload):
        super().__init__(make, model)
        self.payload = payload
```

<br>

### Method overloading

Python does not support method overloading (unless you import some other library). Instead you can assign default value or ```None``` and check for the input value in the function:

```py
    default_nickname = 'Driver'

    #....

    def add_driver(self, name, nickname = None):
        if (nickname == None):
            nickname = self.default_nickname
        
        self.drivers.append(f'{name} {nickname}')
```

```self``` in Python always points to the current instance, even when calling a method on the base class. Whereas in other OOP languages, the base class variables shadows the derived class.

```py
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
```

And when we add driver nickname task we will get:

```py
my_pickup.add_driver('Jane')
my_pickup.add_driver('John', 'Mad Max')
print (my_pickup.drivers) # ['Jane Driver', 'John Mad Max']
```

<br>

## Abstract class

Abstract classes can be inherited, but never instantiated.

To define an Abstract class in Python we should the ```abc``` module.

```py
from abc import ABC, abstractmethod
```

It provides functionality to prevent creating objects from abstract base classes.

```py
from abc import ABC, abstractmethod

class Boat(ABC):
    def __init__(self, id):
        self.id = id

    @abstractmethod
    def calculate_speed(self, value):
        pass

my_boat = Boat(110) # Can't instantiate abstract class Boat with abstract methods calculate_speed
```

A class which is going to extend this base class can do:

```py
class FishingBoat(Boat):

    def __init__(self, id):
        super().__init__(id)

my_fishing_boat = FishingBoat('XYZ551') # Can't instantiate abstract class FishingBoat with abstract methods calculate_speed
```

Because the derived class must override the *Abstract Method* as well:

```py
#...
    def calculate_speed(self, value):
        return value + ' ml'

my_fishing_boat = FishingBoat('XYZ551')
```

<br>

## Multiple Inheritance
> Python is one of the few modern programming languages that supports multiple inheritance.

In most modern OOP languages you are only allowed to inherit from only one base class, but instead you can implement from many **interfaces**.<br>
This is considered a good practice according to **Interface Segregation Principle**.

> Python allows you to inherit from two different classes by specifying them between parenthesis in the class declaration.

```py
class FloatingHoverCar(Boat, Car):

    def __init__(self, id, make, model): # __init__() takes 2 positional arguments but 4 were given
        super().__init__(id, make, model)
    
    def calculate_speed(self, value):
        pass
```

A look into method resolution order will give us:

```bash
 |  Method resolution order:
 |      FloatingHoverCar
 |      Boat
 |      abc.ABC
 |      Car
 |      builtins.object
```

Therefore, we have to bypass this order with directly calling the **Car** ```__init__``` on it's class name:

```py
class FloatingHoverCar(Boat, Car):

    def __init__(self, id, make, model):
        Car.__init__(self, make, model)
        super().__init__(id)
    
    def calculate_speed(self, value):
        pass
```

<br>

<!-- ## Interface -->

### References

* [Inheritance and Composition: A Python OOP Guide](https://realpython.com/inheritance-composition-python/#abstract-base-classes-in-python)