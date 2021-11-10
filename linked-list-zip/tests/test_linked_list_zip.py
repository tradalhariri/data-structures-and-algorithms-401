from linked_list_zip import __version__
from linked_list_zip.linked_list import LinkedList
from linked_list_zip.zip_two_lists import *


def test_version():
    assert __version__ == '0.1.0'


def test_zip_two_linked_lists_are_equal_in_length():
    first = LinkedList()
    first.append(1)
    first.append(3)
    first.append(2)
    first.append(10)
    second = LinkedList()
    second.append(5)
    second.append(9)
    second.append(4)
    second.append(2)

    expected = "{1} -> {5} -> {3} -> {9} -> {2} -> {4} -> {10} -> {2} -> NULL"
    actual = zip_Lists(first, second).__str__()
    assert actual == expected

def test_zip_two_linked_lists_first_less_than_second_in_length():
    first = LinkedList()
    first.append(1)
    first.append(3)
    second = LinkedList()
    second.append(5)
    second.append(9)
    second.append(4)
    second.append(2)

    expected = "{1} -> {5} -> {3} -> {9} -> {4} -> {2} -> NULL"
    actual = zip_Lists(first, second).__str__()
    assert actual == expected

def test_zip_two_linked_lists_second_less_than_first_in_length():
    first = LinkedList()
    first.append(1)
    first.append(3)
    first.append(2)
    first.append(10)
    second = LinkedList()
    second.append(5)
    second.append(9)


    expected = "{1} -> {5} -> {3} -> {9} -> {2} -> {10} -> NULL"
    actual = zip_Lists(first, second).__str__()
    assert actual == expected

def test_zip_two_linked_lists_first_empty():
    first = LinkedList()
    second = LinkedList()
    second.append(5)
    second.append(9)


    expected = "{5} -> {9} -> NULL"
    actual = zip_Lists(first, second).__str__()
    assert actual == expected

def test_zip_two_linked_lists_second_empty():
    first = LinkedList()
    first.append(1)
    first.append(3)
    first.append(2)
    second = LinkedList()
    expected = "{1} -> {3} -> {2} -> NULL"
    actual = zip_Lists(first, second).__str__()
    assert actual == expected

def test_zip_two_linked_lists_two_empty():
    first = LinkedList()
    second = LinkedList()
    expected = "NULL"
    actual = zip_Lists(first, second).__str__()
    assert actual == expected

def test_zip_two_linked_lists_first_one_node():
    first = LinkedList()
    first.append(10)
    second = LinkedList()
    second.append(5)
    second.append(6)
    expected = "{10} -> {5} -> {6} -> NULL"
    actual = zip_Lists(first, second).__str__()
    assert actual == expected

def test_zip_two_linked_lists_second_one_node():
    first = LinkedList()
    first.append(10)
    first.append(6)
    second = LinkedList()
    second.append(5)
    expected = "{10} -> {5} -> {6} -> NULL"
    actual = zip_Lists(first, second).__str__()
    assert actual == expected

def test_zip_two_linked_lists_two_have_one_node():
    first = LinkedList()
    first.append(10)
    second = LinkedList()
    second.append(5)
    expected = "{10} -> {5} -> NULL"
    actual = zip_Lists(first, second).__str__()
    assert actual == expected