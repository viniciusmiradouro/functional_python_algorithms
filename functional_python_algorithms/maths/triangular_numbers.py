from pydantic import PositiveInt


def triangular_number(n: PositiveInt) -> PositiveInt:
    return 1 if n == 1 else n + triangular_number(n - 1)
