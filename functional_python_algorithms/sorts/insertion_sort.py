def insertion_sort(t: tuple[int, ...]) -> tuple[int, ...]:

    def insert(x: int, t: tuple[int, ...]) -> tuple[int, ...]:
        if not t or x <= t[0]:
            return (x,) + t
        return insert(x, t[1:])

    return t if not t else insert(t[0], insertion_sort(t[1:]))
