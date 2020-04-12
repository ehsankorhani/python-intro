# Built-In Functions

Python has many functions that are readily available for use. 

## String built-in methods
String methods returns new values. They do not change the original string.

<br>

**lower()** and **upper**

They convert a string into lower or upper case:

```bash
>>> "ALFIE".lower()
'alfie'

>>> "alfie".upper()
'ALFIE'
```

Inaddition, *isupper()* and *islower()* return a boolean.

<br>

**capitalize()** and **title**

Converts the first character or every first character to upper case:

```bash
>>> "alfie atkins".capitalize()
'Alfie atkins'

>>> "alfie atkins".title()
'Alfie Atkins'
```

*swapcase()* is another similar function.

<br>

**count()**

Number of times a value has appears in the string:

```bash
>>> "the quick brown fox jumps over the lazy dog".count("the")
2
```

<br>

**startswith()** and **endswith()** and **find()**

Return boolean if condition is satisfied or return the index of containing string.

```bash
>>> "Hello Alfie. welcome back.".startswith("Hi")
False

>>> "Hello Alfie. welcome back.".endswith(".")
True

>>> "Hello Alfie. welcome back.".find("welcome")
13

>>> "Hello Alfie. welcome back.".find("Welcome")
-1
```

Also, *index()*.

<br>

**split()** and **join()** and **partition()**

```bash
>>> "Alfie Atkins".split()
['Alfie', 'Atkins']

>>> " ".join(("Hello", ",", "Alfie", "Atkins"))
'Hello , Alfie Atkins'

>>> "Hello Mr. Alfie Atkins".partition("Mr.")
('Hello ', 'Mr.', ' Alfie Atkins')
```

<br>

**strip()**

```bash
>>> "  Alfie Atkins   ".strip()
'Alfie Atkins'
```

<br>

**format()**

Formats the specified value(s) and insert them inside the string's placeholder.

```bash
>>> "The total price will be: {price:.2f}".format(price = 18.5)
'The total price will be: 18.50'
```