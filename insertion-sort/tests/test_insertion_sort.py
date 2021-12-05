from insertion_sort import __version__

from insertion_sort.insertion_sort import insertion_sort
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_empty_list_insertion_sort():
    arr = []
    with pytest.raises(Exception):
        insertion_sort(arr)

def test_insertion_sort():
    arr = [8,4,23,42,16,15]
    insertion_sort(arr)
    assert arr == [4,8,15,16,23,42]

def test_reverse_sorted():
    arr = [20,18,12,8,5,-2]
    insertion_sort(arr)
    assert arr == [-2,5,8,12,18,20]

def test_few_uniques():
    arr = [5,12,7,5,5,7]
    insertion_sort(arr)
    assert arr == [5,5,5,7,7,12]

def test_nearly_sorted():
    arr = [2,3,5,7,13,11]
    insertion_sort(arr)
    assert arr == [2,3,5,7,11,13]