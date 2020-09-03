def f(a: 'some_guide', b: 'more_guide') -> 'return_value':
    pass

print (f.__annotations__)


def f(a: { 'desc': 'full description', 'type': int }) -> float:
    pass

