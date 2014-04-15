try:
    a1 = 42
except:
    a1 = 'spam'
print(a1)

try:
    a2 = 42
except:
    a2 = 'spam'
else:
    a2 = 3.14
print(a2)

try:
    a3 = 42
except:
    a3 = 'spam'
finally:
    a3 = 3.14
print(a3)

try:
    a4 = 42
except:
    a4 = 'spam'
else:
    a4 = 3.14
finally:
    a4 = None
print(a4)

try:
    a5 = 42
    raise AssertionError()
    a5 = 'spam'
except TypeError:
    a5 = 3.14
print(a5)
