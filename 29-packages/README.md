# Packages

Packages are a way of hierarchical structuring Python’s module namespace. Because as the number of modules grows, it becomes hard and inefficient to manage them when they are all located in a same location.

**Packages** help in avoiding module name collisions, as the **modules** are used to avoid collision between global variable names.

Python uses the OS directory structure as the method to create packages. 

```
---- pkg
-------- modules1.py
-------- modules2.py
```

The above demonstrates a package *pkg* that contains two modules.

If directory *pkg* exist in a location that can be found (in any of the ```sys.path``` folders), the modules inside it can be imported with: ```pkg.<module-name>```.

```py
# main.py

import pkg.module1, pkg.module2

pkg.module1.start_engine()
# Toyota Land Cruiser engine started
```

<br>

### References

* [Python Modules and Packages – An Introduction](https://realpython.com/python-modules-packages/)
* [Packages](https://docs.python.org/3/tutorial/modules.html)