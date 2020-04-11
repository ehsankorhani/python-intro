# Type conversion
Like many other programming languages there are two types of *Type* casting in Python:

1. Implicit Type Conversion
2. Explicit Type Conversion

<br>

## Implicit Type Conversion
In this model of casting, Python automatically converts one data type to another data type without programmer's intervention.

Integer to float:

```py
>>> num = 18 # Integer
>>> point = 7.5 # Float
>>> result= num * point
>>> result
135.0
>>> type(result)
<class 'float'>
```

Integer to string:

```py
>>> num = 18 # Integer
>>> name = "Alfie" # String
>>> newName = name + num
TypeError: can only concatenate str (not "int") to str
```

Implicit type cats from *Integer* to *String* is not possible.

## Explicit Type Conversion
Programmer can explicitly convert the data type of an object to the required data type. The following built-in functions are available:

1. str()
2. int(value [,base])
3. float()
4. bool()
5. complex()

**Convert to string:**

```py
>>> num = 18 # Integer
>>> name = "Alfie" # String
>>> newName = name + str(num)
>>> newName
'Alfie18'
```

**Convert to integer:** <br>
```Base``` specifies the base in which a string is converted. By default, ```base``` is set to 10.

```py
>>> int("18")
18

>>> int(18.5)
18

>>>int(True)
1

>>> int("18.5")
ValueError: invalid literal for int() with base 10: '18.5'

>>> int("100", 2)
4

>>> int("Alfie")
ValueError: invalid literal for int() with base 10: 'Alfie'
```

**Convert to float**

```py
>>> float(18)
18.0

>>> float(False)
0.0

>>> float("18.5")
18.5
```

**Convert to boolean** <br>
Any object can be converted to Boolean. In other words, any object has ```truthy``` or ``` falsy``` value.

```py
>>> bool(0)
False
>>> bool(-18)
True
>>> bool(0.1334)
True
>>> bool(0.0)
False
>>> bool(10+8j)
True
>>> bool(0+0j)
False
>>> bool("Alfie")
True
>>> bool(0.0)
False
>>> bool("0")
True
>>> bool(None)
False
>>> bool([])
False
>>> bool([0])
True
```

Other more complex type type conversion also exist in Python. Such as:

* tuple()
* set()
* List()
* dict()

```py
>>> mySet = {"Alfie", "John", "Jane"} 
>>> list(mySet)
['Alfie', 'John', 'Jane']

>>> name = "Alfie"
>>> tuple(name)
('A', 'l', 'f', 'i', 'e')
```

But they only convert compatible types:

```py
>>> dict("Alfie")
ValueError: dictionary update sequence element #0 has length 1; 2 is required
```