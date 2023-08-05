from hypothesis import given
from hypothesis.strategies import lists, integers

from functional_python_algorithms.sorts.quicksort import quicksort

tuples_of_integers = lists(elements=integers()).map(tuple)


@given(tuples_of_integers)
def test_quicksort(tpl):
    sorted_tpl = quicksort(tpl)
    assert len(tpl) == len(sorted_tpl)
    assert tuple(sorted(tpl)) == sorted_tpl
