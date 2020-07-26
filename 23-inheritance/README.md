
# Inheritance

Inheritance definition in Python is also a bit different from the other C-type OOP languages. Rather then extending a Base class, the derived class will receive the Base as a parameter of the class definition.

```py
class Employee:
    firstname = ''
    lastname = ''

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_fullname(self):
        return '{0} {1}'.format(self.firstname, self.lastname)


class Manager(Employee):
    pass
```

At this point *Manager* has access to all the methods and attributes of *Employee*.

```py
mng_1 = Manager('John', 'Doe')

print (mng_1.__dict__) # print (mng_1.__dict__)
print (mng_1.get_fullname()) # John Doe
```

The ```help()``` function can reveal the *Method resolution order* of an instance of *Manager* class.

```py
help(mng_1)

# Method resolution order:
#   Manager
#   Employee
#   builtins.object
```

### Constructor and ```super()```

Derived class can call base class constructor using ```super()```:

```py
class Employee:
    firstname = ''
    lastname = ''

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_fullname(self):
        return '{0} {1}'.format(self.firstname, self.lastname)


class Manager(Employee):
    
    def __init__(self, firstname, lastname, office):
        super().__init__(firstname, lastname)
        #Employee.__init__(self, firstname, lastname)
        self.office = office
```

### Method overloading

Python does not support method overloading (unless you import some other library). Instead you can assign default value or ```None``` and check for the input value in the function:

```py
tasks = []
default_title = 'no name'

#....

def add_task(self, title = None):
    if (title == None):
        self.tasks.append(self.default_title)
    else:
        self.tasks.append(title)
```

```self``` in Python always points to the current instance, even when calling a method on the base class. Whereas in other OOP languages, the base class variables shadows the derived class.

```py
class Employee:
    firstname = ''
    lastname = ''
    tasks = []
    default_title = 'no name'

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_fullname(self):
        return '{0} {1}'.format(self.firstname, self.lastname)

    def add_task(self, title = None):
        if (title == None):
            self.tasks.append(self.default_title)
        else:
            self.tasks.append(title)
    
    def get_tasks(self):
        return self.tasks


class Manager(Employee):
    _meetings = []
    default_title = 'metting'
    
    def __init__(self, firstname, lastname, office):
        super().__init__(firstname, lastname)
        self.office = office
```

And when we add default task we will get:

```py
mng_1 = Manager('John', 'Doe', 'M16')
mng_1.add_task()
print(mng_1.get_tasks()) # ['metting']
```

<br>
