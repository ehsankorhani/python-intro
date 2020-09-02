# Functions
A function is a self-contained block of code that encapsulates a specific task or related group of tasks. Abstraction of functionality into a function is an example of the Don’t Repeat Yourself (DRY) Principle of software development.

In wider programming languages definitions there is another concept called *Procedure* that does not return any value - or the return value is void. In python *Functions* do not specify their return type internally. However this can be achieved with help from some other modules.

There are other things to consider when writing functions. Functions are units of work. The best practice os to not to bloat them with lots of logic. They should do one thing and do that well. Unit-testing approach will help us refactor functions who are not complying with these concepts into smaller peaces.

<br>

## Define a custom function

Just as the other values, a piece of logic can also be associated with name.

```py
def multiply(a, b):
    return a * b
```

The ```def``` keyword tells Python compiler that we have a reusable code.

To use the function:

```py
result = multiply(2, 3)

print(result)
>>> 9
```

<br>

## Parameters

Functions can accept none, one, or many arguments. 

```py
def start():
    print('Engine started!')

def accelerate(current_speed, acceleration_rate, unit):
    print(f'{current_speed * (acceleration_rate + 1)} {unit}')
```

The most common way to pass arguments to a function is with **positional arguments**. When calling the function ```accelerate``` we should pass corresponding values in correct order:

```py
accelerate(100, 0.5, 'km')
# 150.0 km
```

The positional arguments are not flexible. Another approach is to use **keyword arguments**. 

```py
accelerate(acceleration_rate=0.4, unit='km', current_speed=80)
# 112.0 km
```

As you see, the order does not matter. It's more clear what we are passing but it is also way more verbose.

Positional and keyword arguments can be used together, but the positional onces should come first and in order.

```py
accelerate(80, acceleration_rate=0.4, unit='km')
```

<br>

### Default parameters

We can assign a value to an argument in function parameter list. This will serve as it's default value if no value had been passed from the caller.

```py
def accelerate(current_speed, acceleration_rate=0.1, unit='km'):
    print(f'{current_speed * (acceleration_rate + 1)} {unit}')
```

To call the function above the only required value is the ```current_speed```:

```py
accelerate(100)
# 110.00000000000001 km
```

But the default values will overridden if any value has been provided:

```py
accelerate(100, unit='mi')
# 110.00000000000001 mi
```

<br>

### Mutable default parameters

All arguments in the last example were ```immutable``` types. But they can actually hold ```mutable``` types such as ar array.

```py
def createShowroom(cars=[]):
    cars.append('Porsche')
    print(cars)

createShowroom(['BMW', 'Mercedes'])
# ['BMW', 'Mercedes', 'Porsche']
createShowroom(['Honda', 'Mazda'])
# ['Honda', 'Mazda', 'Porsche']
```

But things will get weird if we don't pass any value. In Python, the default value isn’t re-defined each time the function is called.<br>
We can test this by calling ```id(cars)```.

```py
createShowroom()
# ['Porsche']
createShowroom()
# ['Porsche', 'Porsche']
createShowroom()
# ['Porsche', 'Porsche', 'Porsche']
```

A workaround is to set the default value to ```None``` and test variable value for this:


```py
def createShowroom(cars=None):
    if cars is None:
        cars = []
        cars.append('Porsche')

    print(cars)
```

<br>

## The ```return``` statement

The ```return``` statement serves two purposes:

### 1. Terminates the function and passes execution control back to the caller.

```py
def start(hasFuel):
    if not hasFuel:
        return
    
    print('Engine started!')
    return

    print('This line will never get called!')


start(False) # nothing happens
start(True) # Engine started!
```

In this case the value of the return statement is ```None```.

```py
print (start(False)) # None
```

This is similar to when function doesn't return anything:

```py
def f():
    pass

print (f()) # None
```

### 2. Pass data back to the caller.

```py
def accelerate():
    return 'Go faster!'

print (accelerate()) # Go faster!
```

If multiple comma-separated expressions are specified in a return statement, they will be packed and returned as a tuple:

```py
def get_cars():
    return 'Porsche', 'Mercedes', 'BMW'

print (get_cars()) # ('Porsche', 'Mercedes', 'BMW')
```

<br>

## Variables and Scope

<br>

### Global scope
A variable created in the main body of the Python code is a global variable and belongs to the global scope.<br>
This variable can be accessed from within the functions:

```py
def f():
    print (x, id(x)) # 99 9755296

x = 99
print (x, id(x)) # 99 9755296
f()
```

<br>

### Local scope
A variable created inside a function belongs to the local scope of that function. This variable can only be accessed and used inside that function.

```py
def f():
    x = 100
    print (x, id(x)) # 100 9755328

f()
print (x) # NameError: name 'x' is not defined
```

Local variable can override the global variable:

```py
def f():
    x = 100
    print (x, id(x)) # 100 9755328

x = 99
print (x, id(x)) # 99 9755296
f()
print (x, id(x)) # 99 9755296
```

<br>

### Function inside Function

Each function has access to it's own variables and the variables outside of it's definition:

```py
def f():
    x = 100
    print (x, id(x)) # 100 9755328

    def y():
        print (x, id(x)) # 100 9755328

    y()

f()
```

<br>

### Global keyword

The ```global``` keyword makes the variable global, regardless of the place it has been defined:

```py
x = 99 # this will get overridden

def f():
    global x
    x = 100
    print (x, id(x)) # 100 9755328

f()
print (x, id(x)) # 100 9755328
```

<br>

### References

* [Defining Your Own Python Function](https://realpython.com/defining-your-own-python-function/)
* [Python Scope](https://www.w3schools.com/python/python_scope.asp)