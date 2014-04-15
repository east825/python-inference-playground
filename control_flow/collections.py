# only this type will be inferred
d1 = {'foo': 1, 'bar': 2}
print(d1)

d2 = {'foo': 1, 'bar': 'baz'}
print(d2)

d3 = {1: 'foo', 'bar': 'baz'}
print(d3)

d4 = dict(d1)
print(d4)

d5 = dict([(1, 'foo'), (2, 'bar')])
print(d5)

# Why not inferred?
d6 = {x: x**2 for x in range(1)}
print(d6)

d7 = dict.fromkeys('foo')
print(d7)

# type of value is not specified in any way
d7 = dict.fromkeys(range(1))
print(d7)

# only this type will be inferred
l1 = [1, 2, 3]
print(l1)

l2 = [1, 2, 'foo']
print(l2)

x = 1
y = int('10', base=2)
l3 = [x, y, 3]
print(l3)

# Wrong! Impossible list type
l4 = list(d1)
print(l4)

l5 = list(l1)
print(l5)

l6 = [x for x in range(1)]
print(l6)

# type of collections longer than 10 won't be inferred
l4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(l4)

# Why not inferred?
l5 = list('foo')
print(l5)

# only this type will be inferred
s1 = {1, 2, 3}
print(s1)

s2 = {1, 2, 'foo'}
print(s2)

# Why not inferred?
s3 = set(l1)
print(s3)

s4 = set(s1)
print(s1)

# Why not inferred?
s5 = set('foo')
print(s5)

# Why not inferred?
s6 = set(d1)
print(s6)

# Why not inferred?
s7 = {x for x in range(1)}
print(s7)





