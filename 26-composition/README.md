# Composition

> Prefer composition over inheritance - but do not use a compose-always approach.

Composition is a concept that models a ```has a``` relationship. In composition, a class known as *composite* contains an object of another class known to as *component*. 

According to **Liskov substitution principle**; reference to the Base class can be replaced with a Derived class without affecting the functionality of the program.

Therefore, the *Child* class should expose the complete interface of the *Parent* (and more). That makes it fit to derive from Parent.

However, if a classA only requires some behavior of the the classB, then it can use classB as composition.

Problem with *inheritance* is that the sub-class will become bloated with all the implementations of the super-class if it doesn't need them.

<br>

## Implementing composition

We can say that Every *Car* has an *Engine*. The Engin is a separate entity. It can be used totally separated from Car in other devices.

```py
class Engine:

    def __init__(self, capacity, cylinder):
        self.capacity = capacity
        self.cylinder = cylinder

    def start(self):
        print(f'{self.cylinder} cylinder engine started!')
```

We can now add the Engin to the Car class through composition:

```py
class Car():
    
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.engine = None
```

Note that *engine* has been initialized with None. So every instance of *Car* can reference to a different engine.

```py
monsterEngine = Engine(6300, 12)
ecoEngine = Engine(1200, 4)

myFerrari = Car('Ferrari', 'GTC4')
myFerrari.engine = monsterEngine

myFerrari.engine.start() # 12 cylinder engine started!
```

<br>

### References

* [Inheritance and Composition: A Python OOP Guide](https://realpython.com/inheritance-composition-python/#inheriting-multiple-classes)
* [Prefer composition over inheritance?](https://stackoverflow.com/a/53354)