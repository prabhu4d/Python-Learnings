"""
Fixtures are base for test functions, means checking somethings
which is need by test functions

"""

import pytest


class Money:
    def __init__(self):
        self.wallet = []

    def add(self, rupees):
        self.wallet.append(rupees)
        return sum(self.wallet)


# Scope is not defined, so whenever a test functions runs
# this fixtures are runs again
@pytest.fixture
def diff_money():
    print("\n -> Creating Money")
    return Money()


def test_day_1(diff_money):
    print(id(diff_money))
    assert diff_money.add(10) == sum(diff_money.wallet)


def test_day_2(diff_money):
    print(id(diff_money))
    assert diff_money.add(20) == sum(diff_money.wallet)


# Scope is Module, so it only runs once if test functions are in same modules
# if test functions in different modules this fixture reruns
@pytest.fixture(scope="module")
def same_money():
    print("\n -> Same Money")
    return Money()


def test_day_3(same_money):
    print(id(same_money))
    assert same_money.add(10) == sum(same_money.wallet)


def test_day_4(same_money):
    print(id(same_money))
    assert same_money.add(20) == sum(same_money.wallet)
