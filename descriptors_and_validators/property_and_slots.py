# Typical pythonic way to define properties
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError("Age must be an integer")
        if value < 0:
            raise ValueError("Age must be a positive integer")
        self._age = value


class Immutable:

    __slots__ = ('_dept', '_name')          # Replace the instance dictionary

    def __init__(self, dept, name):
        self._dept = dept                   # Store to private attribute
        self._name = name                   # Store to private attribute

    @property                               # Read-only descriptor
    def dept(self):
        return self._dept

    @property
    def name(self):                         # Read-only descriptor
        return self._name



if __name__ == "__main__":
    mark = Immutable("Botany", "Mark Watney")
    print(mark.dept)
    print(mark.name)
    try:
        mark.dept = "Space Pirate"           # Raises AttributeError
    except AttributeError as e:
        print(e)
    try:
        mark.location = "Mars"               # Raises AttributeError
    except AttributeError as e:
        print(e)
    print(mark.dept)
    print(mark.name)