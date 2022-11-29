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
        return reduce((lambda x, y: x * y), args)

    @staticmethod
    def div(a: float, b: float) -> float:
        pass
