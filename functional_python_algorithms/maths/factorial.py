from pydantic import NonNegativeInt as Natural


def factorial(x: Natural) -> Natural:
    return 1 if x == 0 else x * factorial(x - 1)
