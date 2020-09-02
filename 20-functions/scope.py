# def f():
#     print (x, id(x))

# x = 99
# print (x, id(x))
# f()

# # ----------------

# def f():
#     x = 100
#     print (x, id(x))

# f()
# # print (x)

# # ----------------

# def f():
#     x = 100
#     print (x, id(x))

# x = 99
# print (x, id(x))
# f()
# print (x, id(x))

# # ----------------

# def f():
#     x = 100
#     print (x, id(x))

#     def y():
#         print (x, id(x))

#     y()

# f()

# # ----------------

x = 99

def f():
    global x
    x = 100
    print (x, id(x))

f()
print (x, id(x))