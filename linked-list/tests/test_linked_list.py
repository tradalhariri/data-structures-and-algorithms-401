from linked_list import __version__
from linked_list.linked_list import LinkedList
import pytest 


def test_version():
    assert __version__ == '0.1.0'

def test_instantiation_linked_list():
    ll = LinkedList()
    assert ll.head == None

def test_insert_linked_list(ll):
    assert "{12} -> {7} -> {5} -> NULL" == ll.__str__()

def test_head_point_to_first_node(ll):
    assert ll.head.value == 12

def test_insert_multiple_linked_list(ll):
    ll.insert(0)
    ll.insert(-9)
    assert "{-9} -> {0} -> {12} -> {7} -> {5} -> NULL" == ll.__str__()

def test_included_link_list_5(ll):
    assert ll.include(5) == True

def test_included_link_list_100(ll):
    assert ll.include(100) == False

def test_returned_collection():
    ll2 = LinkedList()
    ll2.insert(5)
    ll2.insert(7)
    ll2.insert(12)    
    expected = [12, 7, 5]
    actual = ll2.getCollection()
    assert expected == actual

@pytest.fixture
def ll():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(7)
    ll.insert(12)
    return ll