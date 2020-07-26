# String

The string type in Python is called ```str```. <br>
String literals may be delimited using either single or double quotes.

```bash
>>> type ("Alfie")
<class 'str'>

>>> type('')
<class 'str'>
```

A string can contain as many characters as the computer memory allows.

<br>

## Concatenation

Strings can be concatenated with the ```+``` operator. 

```bash
>>> print ("Nissan" + " " + "Skyline")
Nissan Skyline
>>> make = "Porsche"
>>> model = "911"
>>> print (make + " " + model)
Porsche 911
```

Or with two string literals (not variables) next to each other.

```bash
>>> print ("Nissan" "Skyline")
NissanSkyline
```

```*``` operator repeats a string.

```bash
>>> Print ("BMW"  * 3)
BMW BMW BMW 
```

<br>

## String index

In an string index, first character is having index 0.

```bash
>>> make = "Porsche"
>>> make[0] # first character -> 'P'
>>> make[5] # 5th character -> 'c'
>>> make[-1] # last character -> 'e'
```

Indexing also supports slicing. First value is *included* and second one is *excluded*.

```bash
>>> make = "Porsche"
>>> make[0:3] # 'Por'
>>> make[:3] # 'Por'
>>> make[2:] # 'rsche'
>>> make[:2] + make[2:] # "Porsche
>>> make[:3] + make[3:] # "Porsche
```

Attempting to use an index that is too large will result in an error.

```bash
>>> make = "Porsche"
>>> make[10]
IndexError: string index out of range
```

## Immutability

Strings are immutable and we cannot modify their parts via index position.

```bash
>>> make = "BMW"
>>> make[0] = "A"
TypeError: 'str' object does not support item assignment
```

<br>

## Escape Sequences

Backslash (```\```) character in a string indicates that one or more characters that follow it should be treated specially.

<br>

### Suppressing Special Character

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

<br>

### Applying Special Meaning

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


<br>

## Triple-Quoted Strings

Convenient way to create a multiline string with both single and double quotes in it.

```bash
>>> print("""My name
... is "Alfie".""")
My name
is "Alfie".
```

<br />

## Raw Strings

To not translating escape sequence.

```bash
>>> print(r'Name:\nAlfie')
Name:\nAlfie
```

<br>

## Formatting

```%``` is used for string formatting.

```bash
>>> model = "Skyline"
>>> build_year = 1970
>>> '%s: %d' % (model, build_year)
'Skyline: 1970'
```

Basic arguments in string formatting are:
* %s - String (or any object with a string representation, like numbers)
* %d - Integers
* %f - Floating point numbers
* %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
* %x/%X - Integers in hex representation (lowercase/uppercase)

<br>

## Membership

```in``` and ```not in``` return existence r non-existence of a letter in a string.

```bash
>>> car = "Nissan Skyline"
>>> "Sk" in car
True
>>> "SK" in car
False
```

```bash
>>> car = "Nissan Skyline"
>>> "k" not in car
False
>>> "K" not in car
True
```