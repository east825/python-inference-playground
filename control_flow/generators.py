g1 = (x for x in range(1))
print(g1)

g2 = (x for x in ['foo', 'bar', 'baz'])
print(g2)

g3 = (x for x in {1, None})
print(g3)

def gen1():
    for x in range(1):
        yield x


print(gen1)