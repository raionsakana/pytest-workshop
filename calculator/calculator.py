from functools import reduce


class Calculator:
    @staticmethod
    def add(*args: float) -> float:
        return sum(args)

    @staticmethod
    def sub(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiply(*args: float) -> float:
        if any(i == 0 for i in args):
            raise ValueError('you cannot multiply by 0')

        return reduce((lambda x, y: x * y), args)

    @staticmethod
    def div(a: float, b: float) -> float:
        if b == 0:
            return float('inf')

        return a / b

    @staticmethod
    def avg(a: list[float], ut: float = float('inf'), lt: float = float('-inf')) -> float:
        a = [i for i in a if ut > i > lt]
        return sum(a) / len(a)
