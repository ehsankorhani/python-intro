# Packages

Packages are a way of hierarchical structuring Python’s module namespace. Because as the number of modules grows, it becomes hard and inefficient to manage them when they are all located in a same location.

**Packages** help in avoiding module name collisions, as the **modules** are used to avoid collision between global variable names.

Python uses the OS directory structure as the method to create packages. 

```
---- pkg
-------- modules1.py
-------- modules2.py
main.py
```

The above demonstrates a package *pkg* that contains two modules.

If directory *pkg* exist in a location that can be found (in any of the ```sys.path``` folders), the modules inside it can be imported with: ```pkg.<module-name>```.

```py
# main.py

import pkg.module1, pkg.module2

pkg.module1.start_engine()
# Toyota Land Cruiser engine started
```

All other types of imports are also valid:

```py
# main.py

from pkg.module1 import state_engine()
from pkg.module2 import state_engine() as start_ford()
```

<br>

## Package initialization

Technically the package itself can be imported too. The scripts in file ```__init__.py``` will execute if it exists inside the package folder.

```py
# __init__.py

print (f'Initializing package {__name__}')
cars = ['Toyota', 'Ford']
```

```py
# main.py

import pkg

print (pkg.cars)
```
```
Initializing package pkg

['Toyota', 'Ford']
```

<br>

## Importing ```*``` from a package

When importing all with ```import *``` from a module, all it's objects will be imported - except those that start with an *underscore*. The similar thing can be achieved with packages:

```py
from pkg import *
```

The only feasible use case of this would be to import the required modules automatically by specifying them in ```__init__.py``` file.

```py
# __init__.py

__all__ = ['module1', 'module2']
```

```__all__``` can be used in modules as well to control what to be imported when ```import *```.

> * For a package, when ```__all__``` is not defined, import * does not import anything.
> * For a module, when ```__all__``` is not defined, import * imports everything (except names starting with an underscore).

<br>

## Subpackages

As directories can contain other directories, packages can have sub-packages as well.

```
---- pkg
-------- sub_pkgA
------------ modules1.py
------------ modules2.py
-------- sub_pkgB
------------ modules3.py
------------ modules4.py
main.py
```

There will be an additional **dot notation** when trying to import modules from these packages:

```py
# main.py

import pkg.sub_pkgA.module1
```

Because the modules path is relative to starting script, if a module wants to reference another module it should define the full **dot notation** path and **absolute import**:

```py
# module2.py

from pkg.sub_pkgA.module1 import make
```

Or use the **relative import**:

```py
# module2.py

from ..sub_pkg2.module3 import model
```

>```.``` refers to current directory, ```..``` to the package one level up and ```...``` to two level up.

<br>
<br>

### References

* [Python Modules and Packages – An Introduction](https://realpython.com/python-modules-packages/)
* [Packages](https://docs.python.org/3/tutorial/modules.html)