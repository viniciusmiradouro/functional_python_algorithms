def quicksort(t: tuple[int, ...]) -> tuple[int, ...]:
    if not t or len(t) == 1:
        return t
    minor_partition = tuple(x for x in t[1:] if x <= t[0])
    greater_partition = tuple(x for x in t[1:] if x > t[0])
    return quicksort(minor_partition) + (t[0],) + quicksort(greater_partition)
