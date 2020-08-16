# Classes and Objects

Python supports all OOP features, such as abstraction, inheritance, polymorphism, and encapsulation.

Built-in data structure and collections can be helpful in maintaining a simple state. But for managing more complicated states Classes are better tools. But that's not the only fact about the Classes.

In OOP and Domain-driven-design approach, the Objects should handle the custom behavior. Classes can encapsulate both the behavior and the state.

<br>

## Definition

Classes can simply defined as below:

```py
class Car:
    pass
```

In order to use a class we need to instantiate it:

```py
car1 = Car()
```

Note that unlike other c-type languages there is no need to use the ```new``` keyword.

<br>

### Naming convention

According to **PEP 8**:

> Class names should normally use the **CapWords** convention.
> Class methods should be lowercase with words separated by underscores (i.e. get_name).
> Class instance variables should be lowercase with words separated by underscores (i.e. birth_date)

<br>

### Variable definition

In Python, it's possible to define instance variables directly on the instance:

```py
car1.make = 'Ford'
```

This variable is only owned by the ```car1``` instance. <br>
We can confirm this by using ```__dict__```:

```py
print(Car.__dict__)
print(car.__dict__)
```

```Class``` should act as a blueprint for the objects instantiated from that class.
Therefore, chances are that we prefer to define variables inside the class:

```py
class Car:
    make = ''
```

<br>

## Private and Protected variables and accessors

Generally, unlike most other OOP languages, Python does not encourage the usage of *accessors*. But there are conventions in case they were required.

### Protected variables

> Use one leading underscore only for non-public methods and instance variables.

```py
class Car:
    _odometer = None
```

We can access this value without a problem:

```py
car1 = Car()

print(car1._odometer) # None
```

But we should not. This is a *convention*. 

### Private variables

A double underscore is use to indicate a private attribute.
> To avoid name clashes with subclasses, use two leading underscores to invoke Python's name mangling rules.

```py
class Car:
    __registration_plate = None
```

Now, this value cannot be accessed via:

```py
car1 = Car()

print(car1.__registration_plate) # 'Car' object has no attribute '__registration_plate'
```

Because Python mangles these values with the class name. In this example: ```_Car__registration_plate```.

```py
print(car1._Car__registration_plate) # None
```

Again, as a convention, never use this method ro access a private method.<br>
Private method is only for class internal usage.

### Accessors

Accessors are functions that expose the internal variables to the class outside world

#### Encapsulation
Encapsulation tries to hide the internal logic from outside world:

```py
    def get_odometer(self):
        return f'{self._odometer:,} km'

    def set_odometer(self, value):
        self._odometer = value
```

```py
car1.set_odometer(25800)
print(car1.get_odometer()) # 25,800 km
```

This is a common practice in languages such as C# and Java. It allows actions such as validation on value setting or formatting on get to be performed cleaner.

#### Property attribute

Though the above syntax is valid, there are built-in attribute which allow the class client to access the protected/private variables in a non-function-call manner:

```py
from datetime import datetime

class Vehicle:

    @property
    def rego_expiry(self):
        return f'{self.__rego_expiry} GMT'
    
    @rego_expiry.setter
    def rego_expiry(self, value):
        today = datetime.today().strftime('%Y-%m-%d')
        if (value < today):
            value = 'Expired'
        self.__rego_expiry = value
 
    @rego_expiry.deleter
    def rego_expiry(self):
        del self.__rego_expiry


my_vehicle = Vehicle()

my_vehicle.rego_expiry = '2020-09-15'
print(my_vehicle.rego_expiry)

del my_vehicle.rego_expiry
# print(my_vehicle.rego_expiry) # 'Vehicle' object has no attribute '_Vehicle__rego_expiry'
```

#### Pythonic Way

However, the Pythonic way is not to use any getter or setter. So, this is completely acceptable:

```py
class Car:
    odometer = None

    def __init__(self):
        self.odometer = 0

my_car = Car()

my_car.odometer = 25800
print(my_car.odometer) # 25000
```

<br>

## Methods

Variables are states of an object. Methods add behavior to the object.<br>
In python there are three different method types. The static method, the class method, and the instance method.

```py
class Car:
    make = 'Ford'
    model = 'Ranger'

    def __init__(self):
        pass

    def get_description(self):
        return '{first} {last}'.format(first = Car.make, last = Car.model)
    
    def add_driver(self, name):
        pass
```

<br>

## Constructor

```__init__``` is the constructor of the class and runs when the class is being instantiated. <br>
Though the ```pass``` keyword used here indicates the compiler to pass on this method. ```pass``` is used when we want to define a method but would not want to implement it.

<br>

## Instance variables and ```self``` pointer

```self``` is a pointer to the current instance of the class. Similar to ```this``` keyword in other OOP languages.<br> It can be called anything but the convention is name it *self*.
The difference here is that it has to be included as a parameter on every function.

The important thing to note is that we cannot access the variables inside a class as:

```py
def get_description(self):
    return make + ' ' + model # error
```

The variables are either ```Class``` or ```Instance``` variable.

You define class variables as:

```py
make = 'GMC'
model = 'Suburban'

def get_description(self):
    return Car.make + ' ' + Car.model
```

For the instance variables, there is no need for the variables to have been defined in Class body.

```py
def get_description(self):
    return '{0} {1}'.format(self.make, self.model)
```

So, in the previous example which was using the class variable, the instance cannot change the outcome:

```py
car1 = Car()
car1.make = 'Ford'

print(car1.get_description())
```

The output will be:

```bash
GMC Suburban
```

But if we had written the code as:

```py
class Car:
    make = 'GMC'
    model = 'Suburban'

    def __init__(self):
        pass

    def get_description(self):
        return '{0} {1}'.format(self.make, self.model)    

car1 = Car()
car1.make = 'Ford'

print(car1.get_description())
```

The output would have been:

```bash
Ford Suburban
```

The better practice is to pass parameters to the constructor/methods instead of hard-coding.

```py
class Car:

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_description(self):
        return '{0} {1}'.format(self.make, self.model)

car1 = Car('Ford', 'Ranger')
car2 = Car('Nissan', 'Skyline')

print(car1.get_description()) # Ford Ranger
print(car2.get_description()) # Nissan Skyline
```

<br>

### When to use

There are use cases for Class level variables, such as setting and persisting a value whenever the class was instantiated.

```py
class Car:
    count = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        Car.count += 1


    def get_description(self):
        return '{0} {1}'.format(self.make, self.model)

car1 = Car('Ford', 'Ranger')
car2 = Car('Nissan', 'Skyline')

print(Car.count) # 2
```

<br>

## ClassMethod decorator

Apart from **Class Name** there is a second way to add variables on the class.

Instance methods take the instance (self) as the default first argument.

Class methods should be defined as:

```py
@classmethod
def method_name(cls, param1):
    pass
```

```@classmethod``` is a decorator, and ```cls``` - named by convention - is pointing to the Class.

The class method can then be used to call from the Class and it will affect all the instances: 

```py
...
models = []
...
@classmethod
def add_models(cls, make):
    cls.models.append(make)

...
car1.add_models('BMW')

print(Car.models) # ['BMS']
print(car2.models) # ['BMS']
```

The difference between **@classmethod** and **Class Name** is only in ```inheritance``` and subclassing.

```py
class Car:
    @classmethod
    def use_cls(cls):
        return cls.__name__

    def use_classname(self):
        return Car.__name__

class Pickup(Car):
    pass
```
```py
car = Car()
pickup = Pickup()
```
```py
car.use_cls() # Car
car.use_classname() # Car
pickup.use_cls() # Pickup
pickup.use_classname() # Car
```

<br>

## Static methods

Static methods must be created by decorating the method with:

```py
@staticmethod
def method_name():
    pass
```

We use static methods when we do not require an specific instance to access the method.


```py
class Car:
...
    @staticmethod
    def convert_km_to_mile(value):
        return value / 1.609344

print (Car.convert_km_to_mile(10)) # 6.2137119223733395
```

Unlike most of other OOP languages Static methods can be call on the instance objects as well.

```py
print (car1.convert_km_to_mile(10)) # 6.2137119223733395
```
 
<br>

## Special methods

We can perform **operator overloading** to classes with special methods - also called *magic* or *dunder* methods.

To elaborate, ```+``` sign will perform an *Addition* with Integer types and *Concatenation* with Strings. That is because this operator behavior has been modified in each of these classes.

Special methods which are useful to every class defined are: ```__repr__``` and ```__str__```.

```py
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_description(self):
        return '{0} {1}'.format(self.make, self.model)

    def __repr__(self):
        pass

    def __str__(self):
        pass
```

```__repr__``` is for developers and needs to be unambiguous. ```__str__``` is for the users and should be more readable.

```py
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_description(self):
        return '{0} {1}'.format(self.make, self.model)

    def __repr__(self):
        return "Car('{}', '{}')".format(self.make, self.model)

    def __str__(self):
        return "{} - {}".format(self.make, self.model)

my_car = Car('Ford', 'Ranger')

print(my_car.__repr__()) # Car('Ford', 'Ranger')
print(my_car.__str__()) # Ford - Ranger
```

Other special methods includes ```__add__```, ```__len__```, etc.

```py
def __add__(self, other):
    self.driver + other.driver
```
