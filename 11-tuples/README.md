# Tuples
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