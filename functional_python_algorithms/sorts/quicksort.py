def quicksort(t: tuple) -> tuple:
    if t == () or len(t) == 1:
        return t
    elif len(t) == 2:
        return (t[0], t[1]) if t[0] <= t[1] else (t[1], t[0])
    minor_partition = tuple(filter(lambda x: x <= t[0], t[1:]))
    greater_partition = tuple(filter(lambda x: x >= t[0], t[1:]))
    return quicksort(minor_partition) + (t[0],) + quicksort(greater_partition)
