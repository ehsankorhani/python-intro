def f(**kwargs):
    print (kwargs)
    print (type(kwargs), len(kwargs))

    for key, val in kwargs.items():
        print(key, '->', val)

f(foo=1, bar=2, baz=3)

# --------------------------------------

def f(foo, bar, baz):
    print (foo)

d = {'foo':1, 'bar': 2, 'baz': 3}
f(**d)

# --------------------------------------

def f(**kwargs):
    for k, v in kwargs.items():
        print (k, '->', v)


d1 = {'a': 'foo', 'b': 'bar'}
d2 = {'x': 1, 'y': 2}

f(**d1, **d2)