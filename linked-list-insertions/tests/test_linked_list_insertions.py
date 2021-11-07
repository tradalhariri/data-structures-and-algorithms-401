from linked_list_insertions import __version__
from linked_list_insertions.linked_list import LinkedList
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

# Can successfully add a node to the end of the linked list

# Can successfully add multiple nodes to the end of a linked list

def test_append_node_to_the_end():
    ll = LinkedList()
    ll.append(5)
    ll.append(10)
    ll.append(17)
    assert ll.__str__() == "{5} -> {10} -> {17} -> NULL"

def test_append_multiple_nodes_to_the_end():
    ll = LinkedList()
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.append(0)
    
    assert ll.__str__() == "{5} -> {6} -> {7} -> {0} -> NULL"

def test_insert_before_head():
    ll = LinkedList()
    ll.insert(1)
    ll.insertBefore(1, 18)
    assert ll.__str__() == "{18} -> {1} -> NULL"

def test_insert_before__in_empty_list():
    ll = LinkedList()

    with pytest.raises(Exception):
        ll.insertBefore(1, 18)

def test_insert_before_value_not_exist():
    ll = LinkedList()
    ll.insert(10)
    ll.insert(5)
    ll.insert(6)
    with pytest.raises(Exception):
        ll.insertBefore(11, 18)

def test_insert_before_5():
    ll = LinkedList()
    ll.insert(1)
    ll.append(3)
    ll.append(8)
    ll.insert(9) 
    ll.append(5)
    ll.insertBefore(5, 18)
    assert ll.__str__() == "{9} -> {1} -> {3} -> {8} -> {18} -> {5} -> NULL"
    
def test_insert_before_3():
    ll = LinkedList()
    ll.insert(1)
    ll.append(3)
    ll.append(8)
    ll.insert(9) 
    ll.append(10)
    ll.insertBefore(3, 18)
    assert ll.__str__() == "{9} -> {1} -> {18} -> {3} -> {8} -> {10} -> NULL"

def test_insert_after_10():
    ll = LinkedList()
    ll.insert(1)
    ll.append(3)
    ll.append(10)
    ll.insert(9) 
    ll.append(6)
    ll.insertAfter(10, 15)
    assert ll.__str__() == "{9} -> {1} -> {3} -> {10} -> {15} -> {6} -> NULL"

def test_insert_after__in_empty_list():
    ll = LinkedList()

    with pytest.raises(Exception):
        ll.insertAfter(1, 18)

def test_insert_after_value_not_exist():
    ll = LinkedList()
    ll.insert(10)
    ll.insert(5)
    ll.insert(6)
    with pytest.raises(Exception):
        ll.insertAfter(11, 18)


def test_delete__in_empty_list():
    ll = LinkedList()

    with pytest.raises(Exception):
        ll.deleteNode(18)

def test_delete_value_not_exist():
    ll = LinkedList()
    ll.insert(10)
    ll.insert(5)
    ll.insert(6)
    with pytest.raises(Exception):
        ll.deleteNode(11)

def test_delete_10_node_from_linked_list():
    ll = LinkedList()
    ll.insert(10)
    ll.insert(5)
    ll.insert(6)
    ll.deleteNode(10)
    assert ll.__str__() == "{6} -> {5} -> NULL"

def test_delete_5_node_from_linked_list():
    ll = LinkedList()
    ll.insert(10)
    ll.insert(5)
    ll.insert(6)
    ll.deleteNode(5)
    assert ll.__str__() == "{6} -> {10} -> NULL"

def test_delete_6_node_from_linked_list():
    ll = LinkedList()
    ll.insert(10)
    ll.insert(5)
    ll.insert(6)
    ll.deleteNode(6)
    assert ll.__str__() == "{5} -> {10} -> NULL"

@pytest.fixture
def ll():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(7)
    ll.insert(12)
    return ll