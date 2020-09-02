def start(hasFuel):
    if not hasFuel:
        return
    
    print('Engine started!')
    return

    print('This line will never get called!')

start(False)
start(True)

print (start(False))


def accelerate():
    return 'Go faster!'

print (accelerate())

def get_cars():
    return 'Porsche', 'Mercedes', 'BMW'

print (get_cars())
