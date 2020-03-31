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
Arrays are supported by the array module and need to be imported.

```bash
>>> import array as arr
```

All the entries in an array must be of the same data type. The data type is specified using a type code. 

```bash
>>> marks = arr.array("I", [95, 80, 90])
>>> temps = arr.array("f", [10.5, 18.3])

>>> type(marks)
<class 'array.array'>
```

Arrays are not very popular in Python, and ```Lists``` are a better substitute.

However, Arrays can be helpful in certain cases. For instance, because Arrays only hold one type pf data, some methods are only available for them. For example, converting all the contents to String, etc.

The popular ```NumPy''' library provides a different and much more efficient Array type.

<br />

### Lists
Unlike Arrays, Lists are built-in.


```bash
>>> myList = []
>>> type(myList)
<class 'list'>
```

Lists can be used to store collection of heterogeneous items. 

```bash
>>> myList = list([99, 'Alfie', 10.5])
```

List values can be accessed with a ```zero based``` index.

```bash
>>> myList[0]
99
```

Lists are mutable and their contents can be modified.

```bash
>>> myList[1] = "John"
>>> myList
[99, 'John', 10.5]
```

Many built-in methods are available to work with and manipulate lists. This will be discussed in *built-in functions* sections.

Items are added or removed from a ```List``` according to ```Stacks (LIFO)``` concept.

```bash
>>> stack = ["Red", "Green"]
```

```bash
>>> stack.append("Blue")
>>> print(stack)
["Red", "Green", "Blue"]
```

```bash
>>> stack.pop()
>>> stack.pop()
>>> print(stack)
["Red"]
```

<br>

#### Graphs

> A graph are networks consisting of nodes or vertices which may or may not be connected to each other. The lines or the path that connects two nodes is called an edge. If the edge has a particular direction of flow, then it is a directed graph, with the direction edge being called an arc. Else if no directions are specified, the graph is called an undirected graph.
<br>
datacamp.com

```py
graph = {"Alfie": ["Tom", "John"],
         "Tom": ["Jerry"],
         "John": ["Alfie", "Jerry"]
         }

def define_edges(graph):
    edges = []
    for vertices in graph:
        for neighbour in graph[vertices]:
            edges.append((vertices, neighbour))
    return edges

print(define_edges(graph))
```

```bash
[('Alfie', 'Tom'), ('Alfie', 'John'), ('Tom', 'Jerry'), ('John', 'Alfie'), ('John', 'Jerry')]
```

<br>

#### Tree
Tree can be structured using a combination of other data structures.

<br>

### Tuples
```Tuple``` is an immutable ```list```. It is not possible to delete, add or edit any values inside a tuple once it is defined. 

This is useful when manipulation of the collection data is not desirable when passing it to other methods.

```bash
>>> myTuple_1 = "Alfie","Jane","John"
>>> myTuple_2 = (10.5,15,18)

>>> type(myTuple_1)
<class 'tuple'>

>>> myTuple_1[1]
'Jane'

>>> myTuple_2[0] = 1
TypeError: 'tuple' object does not support item assignment
```

<br>

### Dictionary
Dictionaries are made up of key-value pairs. ```key``` is used to identify the item and the ```value``` holds the value.

Keys should be unique in a dictionary.

```bash
>>> myDict = {"Alfie": 85, "Jane": 95}

>>> type(myDict)
<class 'dict'>

>>> myDict["Alfie"]
85

>>> del myDict["Alfie"]
>>> myDict
{'Jane': 95}
```

<br>

### Sets
Sets are a collection of unique objects. Set is a mutable and unordered list.

```bash
>>> mySet = {"apple", "banana", "cherry"}

>>> type(mySet)
<class 'set'>
```

<br>

### Files
```File``` refers to data stored in computer.

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