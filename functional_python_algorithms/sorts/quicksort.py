def quicksort(t: tuple) -> tuple:
    match t:
        case (pivot, *rest):
            minor_partition = tuple(x for x in rest if x <= pivot)
            greater_partition = tuple(x for x in rest if x > pivot)
            return quicksort(minor_partition) + (pivot,) + quicksort(greater_partition)
        case _:
            return t
