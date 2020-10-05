# Design Patterns

> Design patterns are typical solutions to commonly occurring problems in software design.

<br>

### Categories of patterns

**Creational patterns** provide object creation mechanisms that increase flexibility and reuse of existing code.

**Structural patterns** explain how to assemble objects and classes into larger structures, while keeping the structures flexible and efficient.

**Behavioral patterns** take care of effective communication and the assignment of responsibilities between objects.


<br>

## Table of Contents

1. **Factory method**
2. **Builder**
3. **Singleton**
4. **Strategy**
5. **Iterator**
6. **Observer**
7. **Proxy**
8. **Medatior**
9. **Visitor**
10. **Adapter**
11. **Prototype**
12. **Chain Of Responsibility**
13. **Decorator**
14. **Facade**
15. **Module**

<br>

## Factory method

Is a creational design pattern that provides an interface for creating objects.

The pattern suggests that you replace direct object construction calls (using the ```new``` operator) with calls to a special factory method.

```py
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

my_x5.start() # The v8 engine is starting...
my_miata.start() # The v4 engine is starting...
```

<br>
<br>

---

### References

[Refactoring.Guru Design Patterns](https://refactoring.guru/)