from stack_and_queue.node import Node

from stack_and_queue.empty_stack_except import EmptyStack

class Stack:

    def __init__(self):
        self.top = None
    
    def push(self,value):
        """ push value to the top of stack
        """
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        """ remove the top of stack and return its value
        """
        
        if self.is_empty():
            raise EmptyStack(self.top)
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.value
    
    def peek(self):
        """ return the top value from the stack
        """
        
        if self.is_empty():
            raise EmptyStack(self.top)
        return self.top.value

    def is_empty(self):
        """ check if the stack is empty
        """
        return self.top == None

    def __str__(self):
        """ print stack
        """
        str_stack = f"{{{self.top}}} <-- Top"
        temp = self.top
        while temp.next:
            str_stack = f"{{{temp.next.value}}} <-- " + str_stack
            temp = temp.next
        str_stack= f"NULL <-- "+ str_stack
        return str_stack



if __name__ == '__main__':
    stack = Stack()
    stack.push(4)
    stack.push(5)

    print(stack)

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.peek())