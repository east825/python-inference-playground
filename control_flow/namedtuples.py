from collections import namedtuple

Pair = namedtuple('Pair', ['x', 'y'])

p = Pair(42, 3.14)
print(p)

x, y = p
print(x, y)

x1, y1 = p[0], p[1]
print(x1, y1)

x2, y2 = p.x, p.y
print(x2, y2)