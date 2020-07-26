# Array
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