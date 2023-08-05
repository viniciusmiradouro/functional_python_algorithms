from hypothesis import given
from hypothesis.strategies import lists, integers

from functional_python_algorithms.sorts.insertion_sort import insertion_sort
from functional_python_algorithms.sorts.quicksort import quicksort
from functional_python_algorithms.sorts.bubble_sort import bubble_sort

tuples_of_integers = lists(elements=integers()).map(tuple)


@given(tuples_of_integers)
def test_all_sorts_are_naturally_isomorphic(tpl):
    assert insertion_sort(tpl) == quicksort(tpl) == bubble_sort(tpl)
