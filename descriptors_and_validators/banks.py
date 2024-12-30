from __future__ import annotations
from abc import ABC, abstractmethod


class Validator(ABC):
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, obj, objtype = None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        pass


class BalanceValidator(ABC):
    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Balance must be a number")
        if value < 0:
            raise ValueError("Balance must be a positive number")


class BankAccount:
    balance = BalanceValidator()

    def __init__(self, name: str, balance: int) -> None:
        self.name = name
        self.balance = balance

    def display_balance(self) -> None:
        print(self.balance)
    
    def withraw(self, amount: float | int) -> None:
        self.balance -= amount
    
    def deposit(self, amount: float | int) -> None:
        self.balance += amount

    def transfer(self, amount: float | int, other: BankAccount) ->  BankTransfer:
        return BankTransfer(self, other, amount)

    def __str__(self) -> str:
        return f"{self.name}'s account"


class BankTransfer:
    def __init__(self, from_account: BankAccount, to_account: BankAccount, amount: float) -> None:
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount

    def __call__(self) -> None:
        self.from_account.balance -= self.amount
        self.to_account.balance += self.amount

    def __str__(self) -> str:
        return f"Transfer of {self.amount} from {self.from_account.__str__()} to {self.to_account.__str__()}"


if __name__ == "__main__":
    account1 = BankAccount("James", 100)
    account2 = BankAccount("Bob", 50)
    transfer = account1.transfer(50, account2)
    print(transfer)
    account1.display_balance()
    account2.display_balance()
    