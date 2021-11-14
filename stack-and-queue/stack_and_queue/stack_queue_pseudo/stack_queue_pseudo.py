from stack_and_queue.stack import Stack

class PseudoQueue:

        def __init__(self):
                self.first_stack = Stack()
                self.second_stack = Stack()

        def enqueue(self,value):
             current  = self.second_stack.top
             while current != None:
                     self.first_stack.push (self.second_stack.pop())
                     current = self.second_stack.top

             self.first_stack.push(value)
                     
        def dequeue(self):
             current  = self.first_stack.top
             while current != None:
                     self.second_stack.push ( self.first_stack.pop() )
                     current = self.first_stack.top
             if self.second_stack.top == None:
                     raise  Exception("cant dequeue from empty queue")
             return self.second_stack.pop()
        
        def is_empty(self):
                return self.second_stack.top == None


if __name__ =="__main__":
        pseudo_queue = PseudoQueue()
        pseudo_queue.enqueue(8)
        pseudo_queue.enqueue(9)
        pseudo_queue.enqueue(10)

        print(pseudo_queue.dequeue())

        