# Variables

Variable is a reserved memory location to store values.

## Declaration

Python has no command to declare variables and they are created on the first assignment.

```bash
>>> model = "Skyline"
>>> build_year = 2007
```

Variables can be re-declared and their types can change upon that.

```bash
>>> kilometers = 38000

>>> type (kilometers)
<class 'int'>

>>> kilometers = "38,000 km"

>>> type (kilometers)
<class 'str'>
```

Values can also be assigned to multiple variables in single line.

```bash
>>> make, model, kilometer = "Nissan", "Skyline", 38000
```

<br><br>
## Variable names

Rules for Python variables:

* Must start with a letter or the underscore character.
* Can only contain alpha-numeric characters and underscores.
* Are case-sensitive.

<br><br>
## Concatenate and ```+``` operator

Similar types can be added or concatenated together with ```+``` operator.

```bash
>>> a = True
>>> b = False
>>> a + b
1
```
```bash
>>> a = "Hello"
>>> b = "World"
>>> a + b
'HelloWorld'
```
```bash
>>> a = (1, 2)
>>> b = (3, 4)
>>> a + b
(1, 2, 3, 4)
```

Some non-similar types can also be added together. Python will do the type conversion *implicitly*.

```bash
>>> a = 1
>>> b = True
>>> a + b
2
```

However, non-string variables cannot be concatenated to a string without type conversion.

```bash
>>> a = "Hello"
>>> b = 1
>>> a + b
TypeError: can only concatenate str (not "int") to str
````

Therefore, the concatenation can only implemented with an *explicit* type conversion.

```bash
>>> a = "Hello"
>>> b = 1
>>> a + str(b)
'Hello1'
```

<br><br>
## Local & Global Variables

Variables defined outside of a function are *Global* and the ones defines inside a function are known as *local* variables.

```bash
>>> a = 1 # global
>>> def fn(Self):
...     b = 2 # local

>>> print(a)
1
>>> print(b)
NameError: name 'b' is not defined
```

<br><br>
## Deleting a Variable

Variables can be deleted with ```del``` operator.

```bash
>>> a = "Hello"
>>> b = "World"
>>> del b
>>> a + b
NameError: name 'b' is not defined
```

<br><br>
## Pass-by-object-reference

There are three kinds of *function calls*:

- Pass by value
- Pass by reference
- Pass by object reference

Python is a Pass-by-Object-Reference programming language.

```py
def append(list):
    list.append(1)

list = [0]
append(list)
print (list) # [0, 1]
```

Both the function and the caller refer to the same object in memory. The function and caller use the same object in memory, but accessed through different variables. <br>

The ```list``` variable inside the function is not the same global variable.

Therefore it can be re-assigned without affecting the global variable.

```py
def reassign(list):
    list = [0, 1]

list = [0]
reassign(list)
print (list) # [0]
```

<br><br>
### References
* [Is Python pass-by-reference or pass-by-value?](https://robertheaton.com/2014/02/09/pythons-pass-by-object-reference-as-explained-by-philip-k-dick/)