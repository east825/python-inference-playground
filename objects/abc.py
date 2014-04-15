import abc


class MyABC(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def foo(self):
        pass

    @classmethod
    def __subclasshook__(cls, subclass):
        if 'foo' in vars(subclass):
            return True
        # Unrelated is not considered as subclass of MyABC, if
        # False is returned
        return NotImplemented


class ClassWithFoo:
    def foo(self):
        pass


class SpecialCaseClass:
    pass


class Descendant(MyABC):
    pass


MyABC.register(SpecialCaseClass)

if __name__ == '__main__':
    print(isinstance(ClassWithFoo(), MyABC))
    print(issubclass(ClassWithFoo, MyABC))

    print(isinstance(SpecialCaseClass(), MyABC))
    print(issubclass(SpecialCaseClass, MyABC))

    print(isinstance(Descendant(), MyABC))
    print(issubclass(Descendant, MyABC))
