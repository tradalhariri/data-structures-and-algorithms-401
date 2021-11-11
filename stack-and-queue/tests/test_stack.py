from stack_and_queue.empty_stack_except import EmptyStack

from stack_and_queue.stack import Stack


import pytest

def test_stack_can_push():
    stack = Stack()
    stack.push("hello")
    assert "NULL <-- {hello} <-- Top" == stack.__str__()

def test_stack_can_push_multiple(stack):
    assert "NULL <-- {4} <-- {1} <-- {8} <-- Top" == stack.__str__()

def test_stack_can_pop_off(stack):
    val = stack.pop()
    assert "NULL <-- {4} <-- {1} <-- Top" == stack.__str__()
    assert val == 8

def test_stack_be_empty_after_multiple_pops(stack):
    stack.pop()
    stack.pop()
    stack.pop()
    assert stack.is_empty() == True

def test_stack_can_peek(stack):
    stack.peek()
    assert stack.peek() == 8

def test_can_instatiate_empty_stack():
    stack = Stack()
    assert stack.is_empty() == True

# Calling pop or peek on empty stack raises exception

def test_can_raise_exception_when_pop_or_peek_empty_stack():
    stack = Stack()
    with pytest.raises(EmptyStack):
        stack.pop()
    with pytest.raises(EmptyStack):
        stack.peek()
       
@pytest.fixture
def stack():
    stack = Stack()
    stack.push(4)
    stack.push(1)
    stack.push(8)
    return stack


