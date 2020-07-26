# Boolean

Objects of Boolean type can be ```True``` or ```False```.

```bash
>>> type(True)
<class 'bool'>

>>> type(False)
<class 'bool'>
```

Non-Boolean objects can be evaluated to be true or false as well.

```bash
>>> type(0 < 1)
<class 'bool'>
```

```bash
>>> name = "Alfie"
>>> type (name == "alfie")
<class 'bool'>
```

```bash
>>> teams = ["Chelsea", "Inter Milan"]
>>> type("Chelsea" in teams and "Real Madrid" in teams)
<class 'bool'>
```

Only these values will evaluate to ```False```:

```py
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
```
