from __future__ import annotations

import asyncio
from abc import ABC, abstractmethod
from enum import Enum


class BurgerType(Enum):
    BEEF = "Beef Burger"
    CHEESE = "Cheese Burger"
    CHICKEN = "Chicken Burger"
    VEGGIE = "Veggie Burger"


# 1. Burger interface
class BurgerInterface(ABC):
    @abstractmethod
    def describe(self) -> str: ...

    @abstractmethod
    def cook_time(self) -> int: ...


# 2. Concrete Burger implementations
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
    def create_burger(self, item: BurgerType) -> BurgerInterface: ...

    async def order_burger(self, item: BurgerType) -> BurgerInterface:
        burger = self.create_burger(item)
        print(f"Making a {burger.describe()}")
        await asyncio.sleep(burger.cook_time())
        print(f"Done making a {burger.describe()}")
        return burger


# 4. Concrete Burger Factories
class BeefBurgerStore(BurgerStore):
    def create_burger(self, item: BurgerType) -> BurgerInterface:
        if item == BurgerType.BEEF:
            return BeefBurger()
        elif item == BurgerType.CHEESE:
            return CheeseBurger()
        else:
            raise ValueError(f"Invalid Burger Type: {item}")


class ChickenBurgerStore(BurgerStore):
    def create_burger(self, item: BurgerType) -> BurgerInterface:
        if item == BurgerType.CHICKEN:
            return ChickenBurger()
        else:
            raise ValueError(f"Invalid Burger Type: {item}")


class VeggieBurgerStore(BurgerStore):
    def create_burger(self, item: BurgerType) -> BurgerInterface:
        if item == BurgerType.VEGGIE:
            return VeggieBurger()
        else:
            raise ValueError(f"Invalid Burger Type: {item}")


# Example Usage
async def main():
    beef_store = BeefBurgerStore()
    chicken_store = ChickenBurgerStore()
    veggie_store = VeggieBurgerStore()
    
    # Order different types of burgers concurrently
    await asyncio.gather(
        beef_store.order_burger(BurgerType.BEEF),
        beef_store.order_burger(BurgerType.CHEESE),
        chicken_store.order_burger(BurgerType.CHICKEN),
        veggie_store.order_burger(BurgerType.VEGGIE),
    )

# Run the asyncio program
asyncio.run(main())