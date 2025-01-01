from __future__ import annotations
from abc import ABC, abstractmethod
import time
from enum import Enum


class BurgerType(Enum):
    BEEF = 1
    CHEESE = 2
    CHICKEN = 3
    VEGGIE = 4


# 1. Burger interface
class BurgerInterface(ABC):
    @abstractmethod
    def describe(self): ...

    @abstractmethod
    def cook_time(self): ...


# 2. Concrete Burger
class BeefBurger(BurgerInterface):
    def describe(self) -> str:
        return "Beef Burger"
    
    def cook_time(self) -> int:
        return 3


class CheeseBurger(BurgerInterface):
    def describe(self) -> str:
        return "Cheese Burger"
    
    def cook_time(self) -> int:
        return 4


class ChickenBurger(BurgerInterface):
    def describe(self) -> str:
        return "Chicken Burger"
    
    def cook_time(self) -> int:
        return 3


class VeggieBurger(BurgerInterface):
    def describe(self) -> str:
        return "Veggie Burger"
    
    def cook_time(self) -> int:
        return 2
    

# 3. Burger Factory Interface
class BurgerStore(ABC):
    @abstractmethod
    def create_burger(self, item: BurgerInterface) -> BurgerInterface: ...

    def order_burger(self, item: BurgerInterface) -> BurgerInterface:
        burger = self.create_burger(item)
        print(f"Making a {burger.describe()}")
        time.sleep(burger.cook_time())
        print(f"Done making a {burger.describe()}")
        return burger

# 4. Concrete Burger Factories
class BeefBurgerStore(BurgerStore):
    def create_burger(self, item: BurgerInterface) -> BurgerInterface:
        if item == BurgerType.BEEF:
            return BeefBurger()
        elif item == BurgerType.CHEESE:
            return CheeseBurger()
        else:
            raise ValueError("Invalid Burger Type")


class ChickenBurgerStore(BurgerStore):
    def create_burger(self, item: BurgerInterface) -> BurgerInterface:
        if item == BurgerType.CHICKEN:
            return ChickenBurger()
        else:
            raise ValueError("Invalid Burger Type")


class VeggieBurgerStore(BurgerStore):
    def create_burger(self, item: BurgerInterface) -> BurgerInterface:
        if item == BurgerType.VEGGIE:
            return VeggieBurger()
        else:
            raise ValueError("Invalid Burger Type")
    

if __name__ == "__main__":
    beef_store = BeefBurgerStore()
    beef_store.order_burger(BurgerType.BEEF)
    
    chicken_store = ChickenBurgerStore()
    chicken_store.order_burger(BurgerType.CHICKEN)
    
    veggie_store = VeggieBurgerStore()
    veggie_store.order_burger(BurgerType.VEGGIE)