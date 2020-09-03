def f(fx):
    print (fx, ' reference: ', id(fx))
    fx = 2
    print (fx, ' reference: ', id(fx))

x = 1
f(x)
print (x, ' reference: ', id(x))

# --------------------------

def f(fx):
    print (fx, ' reference: ', id(fx))
    fx = [3, 4]
    print (fx, ' reference: ', id(fx))

x = [1, 2]
f(x)
print (x, ' reference: ', id(x))

# --------------------------

def f(fx):
    print (fx, ' reference: ', id(fx))
    fx.append(3)
    print (fx, ' reference: ', id(fx))

x = [1, 2]
f(x)
print (x, ' reference: ', id(x))

# --------------------------

def f(fx):
    fy = fx.copy()
    fy.append(3)
    print (fx, ' reference: ', id(fx))
    print (fy, ' reference: ', id(fy))

x = [1, 2]
f(x)
print (x, ' reference: ', id(x))
