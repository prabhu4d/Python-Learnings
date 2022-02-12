import numbers
import sys


class CalculatorError(Exception):
    pass


class Calculator:
    def add(self, a, b):
        self._check_operand(a)
        self._check_operand(b)
        return a+b

    def sub(self, a, b):
        return a-b

    def mul(self, a, b):
        return a*b

    def div(self, a, b):
        try:
            return a/b
        except ZeroDivisionError:
            raise CalculatorError("Can't Divide by Zero")
        

    def _check_operand(self, operand):
        if not isinstance(operand, numbers.Number):
            raise CalculatorError(f'{operand} was not a number')


if __name__ == "__main__":
    print("Let's Calculate")
    calcy = Calculator()
    operations = [calcy.add, calcy.sub, calcy.mul, calcy.div]

    while True:
        for i, operation in enumerate(operations, start=1):
            print(f"{i}: {operation.__name__}")
        print("q: quit")
        operation = input("Pick an operation: ")
        if operation == "q":
            sys.exit()
        op = int(operation)
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        try:
            print(operations[op - 1](a, b))
        except CalculatorError as ex:
            print(ex)