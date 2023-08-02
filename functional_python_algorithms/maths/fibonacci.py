from pydantic import NonNegativeInt as Natural


def fibonacci(x: Natural) -> Natural:
    return 1 if x < 3 else fibonacci(x - 2) + fibonacci(x - 1)
