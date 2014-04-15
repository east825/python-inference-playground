def func1(x: int):
    return x


def func2(x: int) -> str:
    return x


# Sphinx format
def func3(x):
    """
    :type x: int
    :rtype: str
    """
    return 'spam'

# Epydoc format
def func3a(x):
    """
    @type x: int
    @rtype: str
    """
    return 'spam'


def func4(x):
    if not isinstance(x, int):
        raise TypeError()
    return x


def func5(x):
    if type(x) != int:
        raise TypeError()
    return x


def func6(x):
    if x.__class__ != int:
        raise TypeError()
    return x


def func7(x):
    return x


func7(42) # int -> int
func7('spam') # str -> str
func7(None) # None -> None


def func8(x=42):
    return x

func9 = lambda x: 'spam' if isinstance(x, int) else None
print(func9)