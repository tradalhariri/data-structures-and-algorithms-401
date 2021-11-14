
from stack_and_queue.stack_queue_pseudo.stack_queue_pseudo import PseudoQueue

import pytest

def test_pseudo_queue_can_enqueue():
    pseudo_queue = PseudoQueue()
    pseudo_queue.enqueue("world")
    assert pseudo_queue.first_stack.top.value == "world"

def test_pseudo_queue_can_enqueue_multiple(pseudo_queue):
    assert pseudo_queue.dequeue() == 8

def test_queue_can_dequeue(pseudo_queue):
    pseudo_queue.dequeue()
  
    assert pseudo_queue.dequeue() == 9


def test_pseudo_queue_be_empty_after_multiple_dequeue(pseudo_queue):
    pseudo_queue.dequeue()
    pseudo_queue.dequeue()
    pseudo_queue.dequeue()
    assert pseudo_queue.is_empty() == True

def test_can_instatiate_empty_pseudo_queue():
    pseudo_queue = PseudoQueue()
    assert pseudo_queue.is_empty() == True

def test_can_raise_exception_when_dequeue_empty_pseudo_queue():
    pseudo_queue = PseudoQueue()
    with pytest.raises(Exception):
        pseudo_queue.dequeue()
       
@pytest.fixture
def pseudo_queue():
    pseudo_queue = PseudoQueue()
    pseudo_queue.enqueue(8)
    pseudo_queue.enqueue(9)
    pseudo_queue.enqueue(10)
    return pseudo_queue