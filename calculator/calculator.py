class Calculator:
    @staticmethod
    def add(*args) -> float:
        return sum(args)

    @staticmethod
    def sub(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b
