# Dictionary
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