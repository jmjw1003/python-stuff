from typing import TypeVar, Generic

"""
Works in a similar way to templates and overloading in C++.
overload can also be imported from typing module and used to define multiple functions with the same name but different signatures.
ie:
@overload
def __init__(self: 'Stack[int]') -> None: ...
(I realise this is completely pointless here)
"""

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self._container = []

    def push(self, item: T):
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self):
        return repr(self._container)


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)
    print(stack.pop())
    print(stack)
    print(stack.pop())
    print(stack.pop())
    print(stack)