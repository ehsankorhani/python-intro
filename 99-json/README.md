# JSON

Python supports JSON with with a built-in package called ```json``` for encoding and decoding JSON data.

```py
import json
```

JSON supports primitive types (string, numbers and boolean), as well as nested lists and objects.

```py
{
    "make": "BMW",
    "model": "X1",
    "navigation": True,
    "odometer": 12050,
    "features": ["Sunroof", "Service History"],
    "engine": {
        "type": "Petrol",
        "capacity": 2500
    },
    "owners": [
        {
            "name": "John Doe",
            "gender": "male"
        }
    ]
}
```

<br>

## Serializing JSON

**Serializing** is the process of **encoding** data into series of bytes,

```dump``` method is used to serialize json into a file on disk:

```py
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)
```

With ```dumps``` you can writes to native Python ```str``` object:

```py
myX1 = json.dumps(dats)
print (myX1)
# {"make": "BMW", "modelX1navigation": true, "odometer": 12050, "features": ["Sunroof", "Service History"], "engine": {"type": "Petrol", "capacity": 2500}, "owners": [{"name": "John Doe", "gender": "male"}]}
```

To make this more readable, we can add a keyword parameter ```indent``` to specify the formatting and whitespace:

```py
myX1 = json.dumps(data, indent=4)
```

Another parameter is ```separators``` which is a ```(item_separator, key_separator)``` tuple.<br>
When ```indent=None``` the default value is: ```(', ', ': ')```.<br>
In other cases the default is ```(',', ': ')```.

To get the most compact JSON representation, you should specify ```(',', ':')``` to eliminate whitespace.

```py
myX1 = json.dumps(data, indent=None, separators=(',', ':'))
```

When serializing, Python objects are translated to JSON according to:

| Python           | JSON          |
| ---------------- |:-------------:|
| dict             | object        |
| list, tuple      | array         |
| str              | string        |
| int, long, float | number        |
| True             | true          |
| False            | false         |
| None             | null          |

<br>

## Deserializing JSON

**Deserialization** is the transformation and **decoding** of bytes into JSON object.

```load``` reads data from file:

```py
with open("data_file.json", "r") as read_file:
    data = json.load(read_file)

print (data) # {'make': 'BMW', 'model': 'X1', ...
```

The result type depends on the input and can be any type. But in most cases it's either ```list``` or ```dict```:

```py
print (type(data)) # <class 'dict'>
```

```loads``` is used to deserialize JSON data when getting data from other parts of code.

```py
response = requests.get("https://www.exampleapi.com/cars")
myCars = json.loads(jsonData)
```

In deserializing the type conversion happens in the reverse order of serializing, with an slight variation:

| JSON           | Python        |
| -------------- |:-------------:|
| array          | list          |
| number (int)   | int           |
| number (real)  | float         |

<br>

## References

* [Working With JSON Data in Python](https://realpython.com/python-json/)
* [JSON encoder and decoder](https://docs.python.org/3/library/json.html)