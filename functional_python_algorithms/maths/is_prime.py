def is_prime(x: int) -> bool:
    return False if -2 < x < 2 else not any(map(lambda d: x % d == 0, range(2, abs(x))))
