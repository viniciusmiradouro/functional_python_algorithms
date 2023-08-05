from hypothesis import given
from hypothesis.strategies import lists, integers

from functional_python_algorithms.sorts.insertion_sort import insertion_sort

tuples_of_integers = lists(elements=integers()).map(tuple)


@given(tuples_of_integers)
def test_insertion_sort(tpl):
    sorted_tpl = insertion_sort(tpl)
    assert len(tpl) == len(sorted_tpl)
    assert tuple(sorted(tpl)) == sorted_tpl
