for _ in range(1):
    if True:
        a1 = 42
        break
else:
    a1 = 'spam'
print(a1)

for _ in range(1):
    if True:
        a2 = 42
else:
    a2 = 'spam'
print(a2)

a3 = 42
for _ in range(1):
    if True:
        a3 = 'spam'
print(a3)

for _ in range(1):
    if True:
        a4 = 42
    else:
        a4 = 'spam'
print(a4)

