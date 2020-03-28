# Beginning Python

## Python interpreter

The python interpreter becomes active when we enter ```python``` in the shell:

```bash
$ python
Python 3.7.3 (default, Mar 27 2019, 22:11:17) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

We can type any valid python expression at the prompt.

```bash
>>> 2 + 3
5
>>> status = True
>>> if status:
...   print("Clear")
Clear
>>>
```

Exit REPL with ```ctrl+D```.

## Python scripts

Create a new file called ```hello-world.py```.

Enter the following in the script file:

```py
sum = -5 + 10

if sum > 0:
    print("Positive number")
else:
    print("negative number")
```

Run the script in shell with:

```bash
$ python hello-world.py
Positive number
```

<br />

## Data types

Function ```type()``` can display the type of the value:

```bash
>>> type(10)
<class 'int'>

>>> type("hello world!")
<class 'str'>

>>> type(True)
<class 'bool'>
```