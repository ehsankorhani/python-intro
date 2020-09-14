make = "Toyota"
model = "Land Cruiser"

def start_engine():
    print (f'{make} {model} engine started')

if (__name__ == '__main__'):
    print('Executing as standalone script')
    print(make)
    start_engine()

from pkg.module2 import make as make2
