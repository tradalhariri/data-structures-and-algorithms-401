from array_insert_shift import __version__
from array_insert_shift.array_insert_shift import insertShiftArray


def test_version():
    assert __version__ == '0.1.0'

def test_insert_shift_array():
    assert [1,2,3,4,5] == insertShiftArray([1,2,4,5],3)
    assert [1,2,3,4,5,6] == insertShiftArray([1,2,3,5,6],4)
    assert [1] == insertShiftArray([],1)
    assert [None] == insertShiftArray([],None)
    assert [1,2] == insertShiftArray([1],2)
    assert [1,2,3] == insertShiftArray([1,3],2)
