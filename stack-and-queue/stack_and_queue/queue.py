from stack_and_queue.node import Node

from stack_and_queue.empty_queue_except import EmptyQueue

class Queue:

    def __init__(self):
        """ initialize Queue method
        """
        self.front = None
        self.rear = None

    def enqueue(self,value):
        """ add new node to the back of the queue
        """
        new_node = Node(value)
        if self.front:
            self.rear.next = new_node
        else:
            self.front = new_node
        self.rear = new_node

    def dequeue(self):
        """ remove node from the front of the queue and return it
        """
        if self.is_empty():
            raise EmptyQueue(self.front)
        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp.value

    def peek(self):
        """ return the value from the front from the queue
        """
        if self.is_empty():
            raise EmptyQueue(self.front)
        return self.front.value

    def is_empty(self):
        """ check if the queue is empty
        """
        return self.front == None

    def __str__(self):
        """ print queue
        """
        str_queue = f"Front --> {{{self.front}}}"
        temp = self.front
        while temp.next:
            str_queue+= f" --> {{{temp.next.value}}}"
            temp = temp.next
        str_queue+= f" --> NULL"
        return str_queue

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.dequeue()
    print (queue)

    print (queue.dequeue())
    print (queue.dequeue())
    print (queue.dequeue())
    print (queue.dequeue())
    print (queue.dequeue())
