from linked_list_kth import __version__
from linked_list_kth.linked_list import LinkedList
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_kth_grater_length_linked_list():
    ll = LinkedList()
    ll.insert(10)
    ll.insert(5)
    ll.insert(6)
    with pytest.raises(Exception):
        ll.kthFromEnd(4)

def test_kth_is_same_length_with_linked_list():
    ll = LinkedList()
    ll.insert(10)
    ll.insert(5)
    ll.insert(6)
    with pytest.raises(Exception):
        ll.kthFromEnd(3)

def test_kth_is_not_positive():
    ll = LinkedList()
    ll.insert(10)
    ll.insert(5)
    ll.insert(6)
    with pytest.raises(Exception):
        ll.kthFromEnd(-3)

def test_linked_list_size_equal_one():
    ll = LinkedList()
    ll.insert(10)
    assert 10 == ll.kthFromEnd(0)

def test_linked_list_size_equal_one_kth_grater_than_length():
    ll = LinkedList()
    ll.insert(10)
    with pytest.raises(Exception):
        ll.kthFromEnd(1)
def test_kth_in_the_middle():
    ll = LinkedList()
    ll.insert(10)
    ll.insert(5)
    ll.insert(3)
    ll.insert(7)
    ll.insert(9)
    assert 3 == ll.kthFromEnd(2)

def test_node_in_the_middle():
    ll = LinkedList()
    ll.insert(10)
    ll.insert(5)
    ll.insert(3)
    ll.insert(7)
    ll.insert(9)
    assert 3 == ll.nodeAtMiddle()
