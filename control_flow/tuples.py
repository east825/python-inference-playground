pair = (41, 'spam')
x1, y1 = pair
print(x1, y1)

# Why not inferred?
x2, *y2 = pair
print(x2, y2)

x3, *y3, z3 = pair
print(x3, y3, z3)

x4 = pair[0]
y4 = pair[1]
print(x4, y4)

pair2 = tuple([1, 2])
print(pair2)

