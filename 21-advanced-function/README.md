# Advanced Function features

## Pass-by-Assignment (Copy-by-Value)

In many OOP programming languages, variable is a reference to a location in memory. That location can have different values, and that value can change. In these languages values are either *Pass-By-Value* or *Pass-By-Reference*.

In Python (and JavaScript and Ruby), variable is a reference pointing to and object. If value of the variable changes, it means it is now pointing to a different object.

Similarly, when passing a value to a function, initially the parameter will point to same value passed, but it can be reassigned:

```py
def f(fx): # fx points to 1. similar to x
    fx = 2 # fx is pointing to the new object 2

x = 1
f(x)
x # is still pointing to 1
```

Lets confirm it by using ```id()``` function.

```py
def f(fx):
    print (id(fx)) # 9752160
    fx = 2
    print (id(fx)) # 9752192

x = 1
f(x)

print (id(x)) # 9752160
```

The ```fx``` reference will not change if we pass value ```2``` to the function:

```py
def f(fx):
    print (id(fx)) # 9752192
    fx = 2
    print (id(fx)) # 9752192

x = 2
f(x)

print (id(x)) # 9752192
```

This will be same for non-primitive types:

```py
def f(fx):
    print (fx, ' reference: ', id(fx)) # [1, 2]  reference:  139716089393024
    fx = [3, 4]
    print (fx, ' reference: ', id(fx)) # [3, 4]  reference:  139716089001280

x = [1, 2]
f(x)

print (x, ' reference: ', id(x)) # [1, 2]  reference:  139716089393024
```

However, if instead of re-assigning, we mutate the value inside the function it will still point to the same object.

```py
def f(fx):
    print (fx, ' reference: ', id(fx)) # [1, 2]  reference:  139716089001280
    fx.append(3)
    # or other mutation operations such as fx[0] = 99
    print (fx, ' reference: ', id(fx)) # [1, 2, 3]  reference:  139716089001280

x = [1, 2]
f(x)

print (x, ' reference: ', id(x)) # [1, 2, 3]  reference:  139716089001280
```

Therefore, in case you're dealing with ```mutable``` types, do not alter them inside the function and instead ```copy``` them into another variable.

```py
fy = fx.copy()
fy.append(3)
```

<br>

## Variable-Length Argument Lists
In some cases, when you’re defining a function, you may not know how many arguments the function should take beforehand.

> Think of ```*args``` as a variable-length positional argument list, and ```**kwargs``` as a variable-length keyword argument list.

<br>

### *args 
If a parameter name is preceded by an asterisk (*), it will be **packed** into a tuple that the function can refer. 

```py
def f(*args):
    print (args)
    print (type(args), len(args))

    for x in args:
        print(x)


f('foo', 'bar', 'baz')
```

```
('foo', 'bar', 'baz')
<class 'tuple'> 3
foo
bar
baz
```

```args``` is a naming convention for this type of parameter (though practically any other name can be used instead).


In addition, when an argument in a function call is preceded by an asterisk (*), it indicates that the argument is an iterable (list, set, tuple) that should be **unpacked** inside the function:

```py
def f(a, b, c):
    print(a) # foo

t = ['foo', 'bar', 'baz']
f(*t)
```

The tuple packing and unpacking can be used together:

```py
def f(*args):
    pass

t = ['foo', 'bar', 'baz']
f(*t)
```

You cannot duplicate the definition of ```*args``` in a function parameter list.

<br>

### *kwargs

The ```*args``` will pack/unpack a tuple. This functionality exist for dictionaries and it is by preceding the parameter with double asterisk (**). It's called ```**kwargs``` by convention.

Below is a demonstration of **Dictionary Packing**:

```py
def f(**kwargs):
    print (kwargs)
    print (type(kwargs), len(kwargs))

    for key, val in kwargs.items():
        print(key, '->', val)

f(foo=1, bar=2, baz=3)
```
```
{'foo': 1, 'bar': 2, 'baz': 3}
<class 'dict'> 3
foo -> 1
bar -> 2
baz -> 3
```

The **Dictionary Unpacking** also works this way:

```py
def f(foo, bar, baz):
    print (foo) # 1

d = {'foo':1, 'bar': 2, 'baz': 3}
f(**d)
```

Note that the dictionary keys should match the function arguments.

<br>

### Multiple unpacking

Multiple unpacking is supported from Python 3.5:

```py
def f(*args):
    for i in args:
        print (i)


a = [1, 2, 3] # List
t = (4, 5, 6) # Tuple
s = {7, 8, 9} # Set

f(*a, *t, *s)
```
```py
def f(*kwargs):
    for k, v in kwargs.items():
        print (k, '->', v)


d1 = {'a': 'foo', 'b': 'bar'}
d2 = {'x': 1, 'y': 2}

f(**d1, **d2)
```

<br>

### Using argument types together

Positional parameters, *args, and **kwargs can be used in one function definition.

```py
def f(a, b, *args, **kwargs):
    pass

f(1, 2, 'foo', 'bar', 'baz', x=88, y=89, z=90)
```

<br>

### Keyword-only arguments

In Python 2.x  it is not possible to define an additional parameter after ```*args```. Python 3.x allow function to take a variable number of arguments, followed by one or more additional options as keyword arguments.

```py
def f(*args, separator='-'):
    pass

f('foo', 'bar', 'baz', separator='_')
```

<br>

### Positional-only parameters

Python 3.8 has added a feature to declare positional-only arguments. To designate some parameters as positional-only, enter a bare slash (/) in the parameter list. Any parameters to the left of the slash (/) must be specified positionally.

```py
def f(a, b, /, c, d):
    print('hello world!')
```

In the examples above, the ```a``` and ```b``` parameters cannot be specified with keywords.

<br>

## Docstrings
A docstring is used to supply documentation for a function. They are string literal defined as the first statement in function body.

```py
def foo(bar=0, baz=1):
    """Perform a foo transformation.

    Keyword arguments:
    bar -- magnitude along the bar axis (default=0)
    baz -- magnitude along the baz axis (default=1)
    """
    # <function_body>
```

When a docstring is defined, the Python interpreter assigns it to a special attribute of the function called ```__doc__```.

```py
print(foo.__doc__)
```
or
```py
help(foo)
```
```
Perform a foo transformation.

    Keyword arguments:
    bar -- magnitude along the bar axis (default=0)
    baz -- magnitude along the baz axis (default=1)
```

<br>

## Function annotations

Python 3.0 introduces another feature for more code readability. *Annotations* attaches a metadata to a function’s parameters and return value.

```py
def f(a: 'some_guide', b: 'more_guide') -> 'return_value':
    pass
```

A special dunder attribute ```__annotations__``` returns a dictionary to display defined annotations.

```py
f.__annotations__
# {'a': 'some_guide', 'b': 'more_guide', 'return': 'return_value'}
```

The annotations can be any expression or object.

```py
def f(a: { 'desc': 'full description', 'type': int }) -> float:
    pass
```

Annotations don’t impose any semantic restrictions. They are only metadata attached to the  function parameters and return value.

<br>
<br>

### References

 * [Defining Your Own Python Function](https://realpython.com/defining-your-own-python-function/)
