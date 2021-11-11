from stack_and_queue.empty_queue_except import EmptyQueue

from stack_and_queue.queue import Queue

import pytest

def test_queue_can_enqueue():
    queue = Queue()
    queue.enqueue("world")
    assert "Front --> {world} --> NULL" == queue.__str__()

def test_queue_can_enqueue_multiple(queue):
    assert "Front --> {8} --> {9} --> {10} --> NULL" == queue.__str__()

def test_queue_can_dequeue(queue):
    val = queue.dequeue()
    assert "Front --> {9} --> {10} --> NULL" == queue.__str__()
    assert val == 8

def test_queue_can_peek(queue):
    assert queue.peek() == 8

def test_queue_be_empty_after_multiple_dequeue(queue):
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    assert queue.is_empty() == True

def test_can_instatiate_empty_queue():
    queue = Queue()
    assert queue.is_empty() == True


def test_can_raise_exception_when_dequeue_or_peek_empty_queue():
    queue = Queue()
    with pytest.raises(EmptyQueue):
        queue.dequeue()
    with pytest.raises(EmptyQueue):
        queue.peek()
       
@pytest.fixture
def queue():
    queue = Queue()
    queue.enqueue(8)
    queue.enqueue(9)
    queue.enqueue(10)
    return queue