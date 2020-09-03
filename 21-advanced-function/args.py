def f(*args):
    print (args)
    print (type(args), len(args))

    for x in args:
        print(x)

f('foo', 'bar', 'baz')

# ------------------------------------

def f(a, b, c):
    print(a)

t = ['foo', 'bar', 'baz']
f(*t)

# ------------------------------------

def f(*args):
    for i in args:
        print (i)


a = [1, 2, 3] # List
t = (4, 5, 6) # Tuple
s = {7, 8, 9} # Set

f(*a, *t, *s)