import sys
import module1

model = 'Rav4'

#from module1 import model
from module1 import model as new_model

print (sys.path)
print (module1.__file__)

#make
module1.make
module1.start_engine()

print(model)
print(new_model)

def accelerate():
    from module1 import make, model
    print (f'{make} {model} is going faster')

accelerate()

try:
    import module1_fake
    from module1 import car
except ImportError:
    print('Module not found')

print (dir())
print (dir(module1))