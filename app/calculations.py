from pickletools import int4


def add(num1: int, num2: 2):
    return num1 + num2


def subtract(num1: int, num2: int):
    return num1 - num2


def multiply(num1: int, num2: int):
    return num1 * num2

def qubic(num1: int, num2: int, num3: int):
    return num1 * num2 * num3


def fourply(num1: int, num2: int, num3: int, num4: int):
    return num1 * num2 * num3 * num4

    
def divide(num1: int, num2: int):
    return num1 / num2

class InsufficientFunds(Exception):
    pass


class BankAccount():
    def __init__(self, starting_balance=0) -> None:
        self.balance = starting_balance
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFunds("Insufficient funds in account")
        self.balance -= amount

    def collect_interest(self):
        self.balance *= 1.1