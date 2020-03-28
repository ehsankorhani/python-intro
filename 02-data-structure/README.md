# Data Structure

Python language does not specify how exactly the memory management should be implemented.

Everything in Python is passed and assigned ```by value```.

**Primitive Data Structures**
* Integers
* Float
* Boolean
* Strings

**Non-Primitive Data Structures**
* Arrays
* Lists
* Tuples
* Dictionary
* Sets
* Files

![Python data structure graph](../images/data-structure.png "Python data structure")


## Primitive data types
<br />

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

<br />

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

<br />

### Boolean

Objects of Boolean type can be ```True``` or ```False```.

```bash
>>> type(True)
<class 'bool'>

>>> type(False)
<class 'bool'>
```

Non-Boolean objects can be evaluated to be true or false as well.

```bash
>>> type(0 < 1)
<class 'bool'>
```

```bash
>>> name = "Alfie"
>>> type (name == "alfie")
<class 'bool'>
```

```bash
>>> teams = ["Chelsea", "Inter Milan"]
>>> type("Chelsea" in teams and "Real Madrid" in teams)
<class 'bool'>
```

<br />

### String

The string type in Python is called ```str```. <br>
String literals may be delimited using either single or double quotes.

```bash
>>> type ("Alfie")
<class 'str'>

>>> type('')
<class 'str'>
```

A string can contain as many characters as the computer memory allows.

#### Escape Sequences

Backslash (```\```) character in a string indicates that one or more characters that follow it should be treated specially.

##### Suppressing Special Character

```bash
>>> print("My name is \"Alfie\".")
My name is "Alfie".
```

To include backslash is a string:

```bash
>>> print("The date was 21\\03\\2020.")
The date was 21\03\2020.
```

And it can also be used to indicate the *newline* should be ignored: 

```bash
>>> print("My \
... name \
... is \
... Alfie.")
My name is Alfie.
```

##### Applying Special Meaning

Backslash can be used to convert the the meaning of a character to something else.

For instance, ```\t``` indicates a ```tab``` space:

```bash
>>> print("Hi \t Alfie.")
Hi       Alfie.
```

Most common ones are:

| Escape Sequence | Interpretation |
| --------------- |:-------------- |
| \n              | New Line       |
| \t              | Tab            |
| \r              | Carriage Return |
| \v              | Vertical Tab   |
| \b              | Backspace      |
| \N{name}        | Character from Unicode with specified name |

<br />

#### Raw Strings

To not translating escape sequence.

```bash
>>> print(r'Name:\nAlfie')
Name:\nAlfie
```

#### Triple-Quoted Strings

Convenient way to create a multiline string with both single and double quotes in it.

```bash
>>> print("""My name
... is "Alfie".""")
My name
is "Alfie".
```

<br />
<br />

## Non-Primitive Data Structures

### Array


### Lists


### Files

<br />
<br />

## Other Data Structures

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

<br />