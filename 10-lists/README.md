# Lists
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