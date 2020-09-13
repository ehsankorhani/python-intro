# Modules

Short applications can be written a single script. As it gets larger it is better to break it into smaller more **maintainable**, more **manageable**, and more **reuseable** chunks. Your scripts might need to access functions and operations from other files.<br>
To achieve this Python has provides a way to put definitions in a file and use them in other scripts via ```import``` statement. Such a file is called a module.
 
With this all individual modules can be put together like building blocks to create a larger application.

There are three ways to define a module:

1. Can be written in Python language.
2. Can be written in ```C``` and loaded dynamically at run-time (i.e. re).    
3. Can be built-in in the interpreter (i.e. itertools).

* check module source with: ```<module-name>.__file__```

<br>

## Python modules

To create a Python module, all that is needed to be done is to create a file that contains Python code and then give the file a name with a ```.py``` extension.

```py
#module1.py

make = "Toyota"
model = "Land Cruiser"

def start_engine():
    print (f'{make} {model} engine started')
```

<br>

## Access a module

All types of modules are accessed the same way: ```import``` statement.


```main.py``` can access ```module1.py``` if they are in same folder with:

```py
# main.py

import module1

module1.start_engine()
```
```
Toyota Land Cruiser engine started
```

<br>

## Module Search Path

When the interpreter executes ```import``` statement, it searches for ```module1.py``` in a list of directories assembled from the following sources:

* Directory from which the input script was run
* Current directory if the interpreter is being run interactively
* List of directories contained in the ```PYTHONPATH``` environment variable

We can view the search path from:

```py
import sys

print (sys.path)
# ['/absolute/path/to/current/directory', '/usr/lib/python38.zip', '/usr/lib/python3.8', '/usr/lib/python3.8/lib-dynload', '/home/eks/.local/lib/python3.8/site-packages', '/usr/local/lib/python3.8/dist-packages', '/usr/lib/python3/dist-packages']
```

Therefore, to ensure the module can be found by the importer:
* Place ```module1.py``` in the directory where the input script is located or in case of interactive run, the current directory
* Modify the ```PYTHONPATH``` environment variable to contain the directory where ```module1.py``` is located
    * before run
    * at run time and before the import statement with: ```sys.path.append(r'/absolute/path/to/current/directory')```


As stated before the path which the module has been imported can be read by:

```py
module1.__file__
# /absolute/path/to/current/directory/module1.py
```

<br>

## The ```import``` statement

This statement creates a separate **namespace** in the caller's symbol table.

```py
# main.py

import module1

make # NameError: name 'make' is not defined
module1.make
```

<br>

### ```from <module_name> import <name(s)>```

Alternatively ```import``` statement allows individual objects from the module to be imported directly into the caller’s symbol table:

```py
# main.py

from module1 import model

print (model)
# Land Cruiser
```

Any objects which already exist with the same name will be overwritten:

```py
# main.py

model = 'Rav4'

from module1 import model

print (model)
# Land Cruiser
```

It is possible to import all objects from the module and place them into caller's local symbol:

```py
# main.py

from module1 import *

make
start_engine()
```

*Note This is not recommended in a large-scale production code.

<br>

### ```from <module_name> import <name> as <alt_name>```

We can rename imported modules before entering them into local symbol table:

```py
# main.py

model = 'Rav4'

from module1 import model as new_model

print(model) # Rav4
print(new_model) # Land Cruiser
```

<br> 

### ```import <module_name> as <alt_name>```

The entire module can be imported under a different namespace:

```py
# main.py

import module1 as mod
```

<br>

### Import withing Function

A module can be imported inside a function definition. The module is inaccessible until the function is executed:

```py
# main.py

def accelerate():
    from module1 import make, model
    print (f'{make} {model} is going faster')

accelerate() # Toyota Land Cruiser is going faster
```

<br>

### Import within ```try``` statement

Try statement can be used to guard against not existent modules or objects:

```py
# main.py

try:
    import module1_fake
    from module1 import car
except ImportError:
    print('Module not found')
```

<br>

## ```dir()``` function

Returns a list of defined names in a namespace.

```py
# main.py

dir()
```
```
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'accelerate', 'model', 'module1', 'new_model', 'sys']
```

```dir()``` can receive an argument which is the name of an imported module. This way, the ```dir()``` returns a list of names defined in the module:

```py
# main.py

import module1

print (dir(module1))
```
```
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'make', 'model', 'start_engine']
```

<br>

## Executing a module as a script

When a module is imported, Python sets the special dunder variable ```__name__``` to the name of the module. But when the file is executed as a script, ```__name__ == '__main__```.

We can use this feature to distinguish and run specific commands only when the file in being run as a script:

```py
# module1.py

make = "Toyota"
model = "Land Cruiser"

def start_engine():
    print (f'{make} {model} engine started')

if (__name__ == '__main__'):
    print('Executing as standalone script')
    print(make)
    start_engine()
```

*This is most useful when *unit testing*.

<br>

## Reloading a module

For efficiency, a module is only loaded once per interpreter session.

```py
# module2.py

make = 'Jaguar'
print (make)
```
```py
# main.py

import module2
# Jaguar
import module2
import module2
```

To force a reload we need to use function ```reload()``` from module ```importlib```:

```py
# main.py

import module2
# Jaguar

import importlib

importlib.reload(module2)
# Jaguar
```

<br>

### References

* [Python Modules and Packages – An Introduction](https://realpython.com/python-modules-packages/)
