def func1(o):
    if o.upper() == 'FOO':
        return o.capitalize()
    return o.strip()


func1(42)

# ABC related tests
from collections.abc import Sized, Iterable, Callable

def func2(xs: Sized):
    return len(xs)


class MySized:
    def __len__(self):
        return 42


func2(42)
func2(MySized())


def func3(xs: Iterable):
    return filter(None, xs)


func3(range(1))
func3('spam')
func3(42)

def func4(f: Callable):
    return f()

class MyCallable():
    def __call__(self, *args, **kwargs):
        pass

func4(map)
func4(MyCallable)
func4(lambda x: x)
func4('foo')
func4([])