from abc import ABCMeta, abstractmethod

class Singleton(metaclass=ABCMeta):
    _instance = None

    @abstractmethod
    def __init__(self):
        pass

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    

class MyClass(Singleton):
    def __init__(self):
        print("MyClass.__init__ called")


def main():
    a = MyClass.get_instance()
    b = MyClass.get_instance()
    assert a is b


if __name__ == "__main__":
    main()
