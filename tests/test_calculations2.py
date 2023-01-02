import pytest
from app.calculations import BankAccount, InsufficientFunds, add, subtract, multiply, divide

@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)

@pytest.mark.parametrize("num1, num2, expected", [
    (3, 2, 5),
    (7, 1, 8),
    (12, 4, 16)
])
def test_add(num1, num2, expected):
    print("testing add function")
    assert add(num1, num2) == expected

def test_subtract():
    assert subtract(9, 4) == 5


def test_multiply():
    assert multiply(9, 4) == 36

def test_divide():
    assert divide(8, 4) == 2




