# Numbers

Python supports two types of numbers - integers and floats.
<br>
Additionally it supports Complex Numbers which are extension of the familiar real number system.

## Integer
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

Result of an integer calculation can be another integer or a float.

```
>>> 5 + 5
10
>>> 10 + 10 * 2 
30
>>> (30 + 10) * 2
80
>>> 80 // 3 # floor
26
>>> 26 % 10 # remainder
6
>>> 6 / 4
1.5
>>> 1.5 ** 4 # to power
5.0625
```

<br />
<br />

## Floating-Point Number

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

