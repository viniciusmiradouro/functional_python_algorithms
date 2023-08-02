def bubble_sort(t: tuple[int, ...]) -> tuple[int, ...]:

    def pairwise_sort(t: tuple[int, ...]) -> tuple[int, ...]:
        if not t or len(t) == 1:
            return t
        if t[0] > t[1]:
            return (t[1],) + pairwise_sort((t[0],) + t[2:])
        return (t[0],) + pairwise_sort(t[1:])

    return t if t == pairwise_sort(t) else bubble_sort(pairwise_sort(t))
