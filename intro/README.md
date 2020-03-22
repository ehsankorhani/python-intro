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

### Integer
There is effectively no limit - except system memory - to how long an integer value can be.

```bash
>>> print(123456789123456789123456789123456789123456789 + 1)
123456789123456789123456789123456789123456790
``` 

To change the integer base:

| Prefix        | Base |
| ------------- |:----:|
| 0b / 0B       | 2    |
| 0o / 0O       | 8    |
| 0x / 0X       | 16   |

examples:

```bash
>>> 0b10
2
>>> 0o10
8
>>> 0x10
16

>>> type(0x10)
<class 'int'>
```

### Floating-Point Number

Python float are represents as 64bit values. Therefore, the maximum value of a floating-point number can be ```1.8 ⨉ 10^308```. <br />

Float values are specified with a decimal point. 
To specify scientific notation add character *e* or *E* followed by a positive or negative number:

```bash
>>> type(10.5)
<class 'float'>

>>> 10e3
10000.0

>>> 10e+3
10000.0

>>> 10e-3
0.01
```

A value greater than the maximum possible will be indicated as string *inf*:

```bash
>>> 10e+308
inf
```

Anything less than ```5.0 ⨉ 10^-324``` is considered to be zero.

```bash
>>> 1e-325
0.0
```

Because floating-points are represented internally as ```binary```, the actual and represented values can be slightly different.

### Complex number
Are specified as ```<real-part>+<imaginary-part>j```:

```bash
>>> 10 + 2j
(10+2j)

>>> x = 10 + 2j
>>> x.real
10.0
>>> x.imag
2.0
>>> x.conjugate()
(10-2j)
```

Complex number can also get created using complex() function:

```bash
>>> complex(10, 2)
(10+2j)
```

Complex numbers are useful in many applications related to mathematics and are mostly used where we define something using two real numbers. For example, a circuit element that is defined by Voltage (V) and Current (I).

```bash
>>> abs(10+2j)
10.198039027185569
```

The absolute value of a complex number ```x+yi``` is ```sqrt((x^2) + (y^2))```.

### Boolean

### String

### Build-in functions

