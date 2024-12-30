import os

class Setting:
    def __init__(self, key: str, *, default: str) -> None:
        self.key = key
        self.default = default
    
    # Overriding __get__ method to get the value of the key from the environment variables
    def __get__(self, obj: object, obj_type: type | None = None) -> str:
        return os.environ.get(self.key, self.default)


class Config:
    TEST = Setting(key="TEST", default="test")  # Simulated getting an environment variable, etc in the form key, value


if __name__ == "__main__":
    print(Config.TEST)

"""
Config.TEST is statically always a string, ie strongly typed conditions are met
Lazy loading condition is satisfied because creating the instance of the Setting class does not run the __get__ method
(You can test that by remove line 18 and replacing with Config)
"""