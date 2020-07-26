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