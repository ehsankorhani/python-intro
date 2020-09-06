<!-- In Python 3, lists get a copy method (in 2, you'd use a slice to make a copy):

>>> a_list = list('abc')
>>> a_copy_of_a_list = a_list.copy()
>>> a_copy_of_a_list is a_list
False
>>> a_copy_of_a_list == a_list
True
Shallow Copies
Shallow copies are just copies of the outermost container.

list.copy is a shallow copy:

>>> list_of_dict_of_set = [{'foo': set('abc')}]
>>> lodos_copy = list_of_dict_of_set.copy()
>>> lodos_copy[0]['foo'].pop()
'c'
>>> lodos_copy
[{'foo': {'b', 'a'}}]
>>> list_of_dict_of_set
[{'foo': {'b', 'a'}}]
You don't get a copy of the interior objects. They're the same object - so when they're mutated, the change shows up in both containers.

Deep copies
Deep copies are recursive copies of each interior object.

>>> lodos_deep_copy = copy.deepcopy(list_of_dict_of_set)
>>> lodos_deep_copy[0]['foo'].add('c')
>>> lodos_deep_copy
[{'foo': {'c', 'b', 'a'}}]
>>> list_of_dict_of_set
[{'foo': {'b', 'a'}}]
Changes are not reflected in the original, only in the copy.

Immutable objects
Immutable objects do not usually need to be copied. In fact, if you try to, Python will just give you the original object:

>>> a_tuple = tuple('abc')
>>> tuple_copy_attempt = a_tuple.copy()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'copy'
Tuples don't even have a copy method, so let's try it with a slice:

>>> tuple_copy_attempt = a_tuple[:]
But we see it's the same object:

>>> tuple_copy_attempt is a_tuple
True
Similarly for strings:

>>> s = 'abc'
>>> s0 = s[:]
>>> s == s0
True
>>> s is s0
True
and for frozensets, even though they have a copy method:

>>> a_frozenset = frozenset('abc')
>>> frozenset_copy_attempt = a_frozenset.copy()
>>> frozenset_copy_attempt is a_frozenset
True
When to copy immutable objects
Immutable objects should be copied if you need a mutable interior object copied.

>>> tuple_of_list = [],
>>> copy_of_tuple_of_list = tuple_of_list[:]
>>> copy_of_tuple_of_list[0].append('a')
>>> copy_of_tuple_of_list
(['a'],)
>>> tuple_of_list
(['a'],)
>>> deepcopy_of_tuple_of_list = copy.deepcopy(tuple_of_list)
>>> deepcopy_of_tuple_of_list[0].append('b')
>>> deepcopy_of_tuple_of_list
(['a', 'b'],)
>>> tuple_of_list
(['a'],)
As we can see, when the interior object of the copy is mutated, the original does not change.

Custom Objects
Custom objects usually store data in a __dict__ attribute or in __slots__ (a tuple-like memory structure.)

To make a copyable object, define __copy__ (for shallow copies) and/or __deepcopy__ (for deep copies).

from copy import copy, deepcopy

class Copyable:
    __slots__ = 'a', '__dict__'
    def __init__(self, a, b):
        self.a, self.b = a, b
    def __copy__(self):
        return type(self)(self.a, self.b)
    def __deepcopy__(self, memo): # memo is a dict of id's to copies
        id_self = id(self)        # memoization avoids unnecesary recursion
        _copy = memo.get(id_self)
        if _copy is None:
            _copy = type(self)(
                deepcopy(self.a, memo), 
                deepcopy(self.b, memo))
            memo[id_self] = _copy 
        return _copy
Note that deepcopy keeps a memoization dictionary of id(original) (or identity numbers) to copies. To enjoy good behavior with recursive data structures, make sure you haven't already made a copy, and if you have, return that.

So let's make an object:

>>> c1 = Copyable(1, [2])
And copy makes a shallow copy:

>>> c2 = copy(c1)
>>> c1 is c2
False
>>> c2.b.append(3)
>>> c1.b
[2, 3]
And deepcopy now makes a deep copy:

>>> c3 = deepcopy(c1)
>>> c3.b.append(4)
>>> c1.b
[2, 3] -->

### References

* [How can I create a copy of an object in Python?](https://stackoverflow.com/a/46939443)