from merge_sort import __version__

from merge_sort.merge_sort import merge_sort



def test_version():
    assert __version__ == '0.1.0'


def test_merge_sort():
    arr = [8,4,23,42,16,15]
    merge_sort(arr)
    assert arr == [4,8,15,16,23,42]

def test_reverse_sorted():
    arr = [20,18,12,8,5,-2]
    merge_sort(arr)
    assert arr == [-2,5,8,12,18,20]

def test_few_uniques():
    arr = [5,12,7,5,5,7]
    merge_sort(arr)
    assert arr == [5,5,5,7,7,12]

def test_nearly_sorted():
    arr = [2,3,5,7,13,11]
    merge_sort(arr)
    assert arr == [2,3,5,7,11,13]
