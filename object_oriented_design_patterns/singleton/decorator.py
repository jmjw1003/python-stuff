def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class MyClass:
    def __init__(self):
        print("MyClass.__init__ called")

def main():
    a = MyClass()
    b = MyClass()
    assert a is b

if __name__ == "__main__":
    main()
