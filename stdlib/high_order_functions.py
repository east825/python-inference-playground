xs1 = map(lambda x: 42, range(1))
print(xs1)

xs2 = filter(lambda x: False, range(1))
print(xs2)

xs3 = zip(range(1), 'foo')
print(xs3)

from functools import reduce
xs4 = reduce(lambda x, y: x + y, range(1), 0)
print(xs4)