
# Advanced Numbers

## Bitwise operations

Bitwise operations is only possible on integers. The result will be calculated as though carried out in two’s complement with an infinite number of sign bits.

| Operation  | Result                          | Example with x=1, y=2, n=10 |
| ---------- | :------------------------------ | :-------------------------- |
| x | y      | bitwise or of x and y           | 3                           |
| x ^ y      | bitwise exclusive or of x and y | 3                           |
| x & y      | bitwise and of x and y          | 0                           |
| x << n     | x shifted left by n bits        | 1024                        |
| x >> n     | x shifted right by n bits       | 0                           |
| ~x         | the bits of x inverted          | -2                          |


<br><br>
## Integer methods

**int.bit_length()**

**int.to_bytes()**

**int.from_bytes()**

<br><br>
## Float methods

**float.is_integer()**

**float.hex()**


<br><br>
## Complex number
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

<br><br>
### References
* [Numeric Types](https://docs.python.org/3/library/stdtypes.html#typesnumeric)