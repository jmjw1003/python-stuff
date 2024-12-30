class AgeValidator:
    def __get__(self, obj: "Person", obj_type: type | None = None) -> int:  # object is the Person instance, obj_type is the Person class
        return obj._age
    
    def __set__(self, obj: "Person", value: int) -> None:
        if not isinstance(value, int):
            raise ValueError("Age must be an integer")
        if value < 0:
            raise ValueError("Age must be a positive integer")
        obj._age = value


class Person:
    _age: int
    age = AgeValidator()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


if __name__ == "__main__":
    person = Person("James", 30)
    print(person.age)
    person.age = 40
    print(person.age)
    try:
        person.age = -1  # Raises ValueError because of the validator
    except ValueError as e:
        print(e)
    print(person.age)